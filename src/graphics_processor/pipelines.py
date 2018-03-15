import os.path
currentdir = os.curdir

from PIL import Image

from graphics_processor import graphics_constants
from graphics_processor.pixa import Spritesheet, pixascan
from graphics_processor.units import SimpleRecolour, SwapCompanyColours, AppendToSpritesheet

DOS_PALETTE = Image.open('palette_key.png').palette

"""
Pipelines can be dedicated to a single task such as simple recolouring
Or they can compose units for more complicated tasks, such as colouring and loading a specific vehicle type
As of Jan 2018 there is just one complex pipeline for ships, which handles hull compositing + optional cargo provision
"""


class Pipeline(object):
    def __init__(self, name):
        # this should be sparse, don't store any ship or variant info in Pipelines, pass them at render time
        self.name = name

    def make_spritesheet_from_image(self, input_image):
        spritesheet = Spritesheet(width=input_image.size[0], height=input_image.size[1] , palette=DOS_PALETTE)
        spritesheet.sprites.paste(input_image)
        return spritesheet

    @property
    def ship_template_input_path(self):
        # convenience method to get the ship template
        # I considered having this return the Image, not just the path, but it's not saving much, and is less obvious what it does when used
        return os.path.join(currentdir, 'src', 'graphics', graphics_constants.vehicles_input_dir, self.ship.id + '.png')

    def render_common(self, variant, ship, input_image, units):
        # expects to be passed a PIL Image object
        # units is a list of objects, with their config data already baked in (don't have to pass anything to units except the spritesheet)
        # each unit is then called in order, passing in and returning a pixa SpriteSheet
        # finally the spritesheet is saved
        output_path = os.path.join(currentdir, 'generated', 'graphics', variant.get_spritesheet_name(ship))
        spritesheet = self.make_spritesheet_from_image(input_image)

        for unit in units:
            spritesheet = unit.render(spritesheet)
        # I don't normally leave commented-out code behind, but I'm bored of looking in the PIL docs for how to show the image during compile
        #spritesheet.sprites.show()
        spritesheet.save(output_path)

    def render(self, variant, ship):
        raise NotImplementedError("Implement me in %s" % repr(self))

class ExamplePassThroughPipeline(Pipeline):
    # example sparse pipeline, does nothing, left in place as example
    def __init__(self):
        # this should be sparse, don't store any ship or variant info in Pipelines, pass them at render time
        super().__init__("pass_through_pipeline")

    def render(self, variant, ship, global_constants):
        input_image = Image.open(self.ship_template_input_path)
        units = []
        result = self.render_common(variant, ship, input_image, units)
        return result


class ExtendSpriterowsForCompositedCargosPipeline(Pipeline):
    """"
        Extends a cargo carrier spritesheet with variations on cargo colours.
        Quite convoluted as it handles multiple classes of cargo (bulk, piece etc)
    """
    def __init__(self):
        # this should be sparse, don't store any ship or variant info in Pipelines, pass them at render time
        # initing things here is proven to have unexpected results, as the processor will be shared across multiple vehicles
        super().__init__("extend_spriterows_for_composited_cargos_pipeline")

    def extend_base_image_to_3_rows_with_waterline_masked_per_load_state(self, base_image):
        # This composites the ship from:
        # - the ship base image (this contains the detail for the specific ship such as wheelhouse, holds etc)
        # - a standard hull image
        # - a waterline mask for each of 'loading' and 'loaded' states
        # And returns 3 rows, masked at the waterline for each of 3 load states
        crop_box_mask_1 = (0,
                           10,
                           graphics_constants.spritesheet_width,
                           10 + graphics_constants.spriterow_height)
        crop_box_mask_2 = (0,
                           10 + graphics_constants.spriterow_height,
                           graphics_constants.spritesheet_width,
                           10 + (2 * graphics_constants.spriterow_height))

        crop_box_ship_base = (0,
                               0,
                               graphics_constants.spritesheet_width,
                               graphics_constants.spriterow_height)

        hull_base = Image.open(self.hull_input_path).crop(crop_box_mask_1)
        # hull_base uses false colour pixels for establishing correct dimensions; make these blue
        hull_base = hull_base.point(lambda i: 0 if (i in range(215, 227) or i == 244) else i)

        # the ship image has false colour pixels for the hull, to aid drawing; remove these by converting to white, also convert any blue to white
        ship_base = base_image.point(lambda i: 255 if (i in range(178, 192) or i == 0) else i)
        # create a mask so that we paste only the ship pixels over the hull (no blue pixels)
        ship_mask = ship_base.copy()
        ship_mask = ship_mask.point(lambda i: 0 if i == 255 else 255).convert("1") # the inversion here of blue and white looks a bit odd, but potato / potato

        hull_base.paste(ship_base, crop_box_ship_base, ship_mask)

        # no hull mask used for first load state (row 1), so only need to create 2 hull mask images
        waterline_mask_row_2 = Image.open(self.waterline_mask_input_path).crop(crop_box_mask_1).point(lambda i: 0 if i == 226 else 255).convert("1")
        waterline_mask_row_3 = Image.open(self.waterline_mask_input_path).crop(crop_box_mask_2).point(lambda i: 0 if i == 226 else 255).convert("1")

        # 3 different load states to composite into result image so 3 different crop boxes to make the rows
        crop_box_comp_dest_1 = (0,
                                0,
                                graphics_constants.spritesheet_width,
                                graphics_constants.spriterow_height)
        crop_box_comp_dest_2 = (0,
                                graphics_constants.spriterow_height,
                                graphics_constants.spritesheet_width,
                                2 * graphics_constants.spriterow_height)
        crop_box_comp_dest_3 = (0,
                                2 * graphics_constants.spriterow_height,
                                graphics_constants.spritesheet_width,
                                3 * graphics_constants.spriterow_height)

        result_image = Image.new("P", (graphics_constants.spritesheet_width, 3 * graphics_constants.spriterow_height))
        result_image.putpalette(DOS_PALETTE)
        result_image.paste(hull_base, crop_box_comp_dest_1) # by design, no mask needed for first load state
        result_image.paste(hull_base, crop_box_comp_dest_2, waterline_mask_row_2)
        result_image.paste(hull_base, crop_box_comp_dest_3, waterline_mask_row_3)
        return result_image

    def add_generic_spriterow(self):
        crop_box = (0,
                    0,
                    graphics_constants.spritesheet_width,
                    graphics_constants.spriterow_height)
        vehicle_generic_spriterow_input_image = self.vehicle_base_image.crop(crop_box)
        # vehicle_generic_spriterow_input_image.show() # comment in to see the image when debugging
        vehicle_generic_spriterow_input_as_spritesheet = self.make_spritesheet_from_image(vehicle_generic_spriterow_input_image)
        self.units.append(AppendToSpritesheet(vehicle_generic_spriterow_input_as_spritesheet, crop_box))

    def add_livery_only_spriterows(self):
        # this might be extensible for containers when needed, using simple conditionals
        # or because containers include random options it might need reworking,
        # to be more similar to piece cargo handling, but using recolour not actual sprites
        vehicle_livery_row_image_as_spritesheet = self.make_spritesheet_from_image(self.vehicle_base_image)

        for label, recolour_map in self.ship.gestalt_graphics.recolour_maps:
            crop_box_dest = (0,
                             0,
                             graphics_constants.spritesheet_width,
                             3 * graphics_constants.spriterow_height)
            self.units.append(AppendToSpritesheet(vehicle_livery_row_image_as_spritesheet, crop_box_dest))
            self.units.append(SimpleRecolour(recolour_map))

    def add_bulk_cargo_spriterows(self):
        cargo_group_row_height = 2 * graphics_constants.spriterow_height
        crop_box_source = (0,
                           self.base_offset,
                           graphics_constants.spritesheet_width,
                           self.base_offset + cargo_group_row_height)
        vehicle_bulk_cargo_image = Image.open(self.ship_template_input_path).crop(crop_box_source)
        vehicle_bulk_cargo_image = vehicle_bulk_cargo_image.point(lambda i: 255 if (i in range(178, 192) or i == 0) else i)
        vehicle_bulk_cargo_mask = vehicle_bulk_cargo_image.copy().point(lambda i: 255 if i == 255 else 0).convert("1")

        vehicle_base_image = self.vehicle_base_image.copy().crop((0, 100, graphics_constants.spritesheet_width, 300))

        vehicle_bulk_cargo_image.paste(vehicle_base_image, None, vehicle_bulk_cargo_mask)
        #vehicle_bulk_cargo_image.show()

        vehicle_bulk_cargo_input_as_spritesheet = self.make_spritesheet_from_image(vehicle_bulk_cargo_image)
        crop_box_dest = (0,
                         0,
                         graphics_constants.spritesheet_width,
                         cargo_group_row_height)
        for label, recolour_map in graphics_constants.bulk_cargo_recolour_maps:
            self.units.append(AppendToSpritesheet(vehicle_bulk_cargo_input_as_spritesheet, crop_box_dest))
            self.units.append(SimpleRecolour(recolour_map))
            self.units.append(SimpleRecolour(recolour_map=self.ship.gestalt_graphics.hull_recolour_map))

    def add_piece_cargo_spriterows(self, global_constants):
        # hax
        print('add_piece_cargo_spriterows: hax to crop out self.vehicle_base_image')
        self.vehicle_base_image = self.vehicle_base_image.copy().crop((0, 100, graphics_constants.spritesheet_width, 300))
        #self.vehicle_base_image.show()
        # !! this could possibly be optimised by slicing all the cargos once, globally, instead of per-unit
        cargo_group_output_row_height = 2 * graphics_constants.spriterow_height
        # Cargo spritesheets provide multiple lengths, using a specific format of rows
        # given a base set, find the bounding boxes for the rows per length
        cargo_spritesheet_bounding_boxes_base = ((10, 10, 18, 24), (28, 10, 42, 22), (50, 10, 66, 20), (72, 10, 86, 22))
        cargo_spritesheet_bounding_boxes = {}
        for counter, length in enumerate([3, 4]):
            bb_result = []
            for y_offset in [0, 20]:
                bb_y_offset = (counter * 40) + y_offset
                bb_result.append(tuple([(i[0], i[1] + bb_y_offset, i[2], i[3] + bb_y_offset) for i in cargo_spritesheet_bounding_boxes_base]))
            cargo_spritesheet_bounding_boxes[length] = bb_result
        # Overview
        # 2 spriterows for the vehicle loading / loaded states, with pink loc points for cargo
        # a mask row for the vehicle, with pink mask area, which is converted to black and white mask image
        # an overlay for the vehicle, created from the vehicle empty state spriterow, and comped with the mask after each cargo has been placed
        # there is a case not handled, where long cargo sprites will cabbed vehicles in / direction with cab at N end, hard to solve
        crop_box_vehicle_cargo_loc_row = (0,
                           self.base_offset,
                           graphics_constants.spritesheet_width,
                           self.base_offset + graphics_constants.spriterow_height)
        vehicle_cargo_loc_image = Image.open(self.ship_template_input_path).crop(crop_box_vehicle_cargo_loc_row)
        # get the loc points
        loc_points = [pixel for pixel in pixascan(vehicle_cargo_loc_image) if pixel[2] == 226]
        # two cargo rows needed, so extend the loc points list
        loc_points.extend([(pixel[0], pixel[1] + graphics_constants.spriterow_height, pixel[2]) for pixel in loc_points])
        # sort them in y order, this causes sprites to overlap correctly when there are multiple loc points for an angle
        loc_points = sorted(loc_points, key=lambda x: x[1])
        crop_box_mask = (0,
                         10 + (4 * graphics_constants.spriterow_height),
                         graphics_constants.spritesheet_width,
                         10 + (5 * graphics_constants.spriterow_height))
        vehicle_mask_base_image = Image.open(self.ship_template_input_path).crop(crop_box_mask).point(lambda i: 255 if i == 226 else 0).convert("1")
        vehicle_mask = Image.new("1", (graphics_constants.spritesheet_width, cargo_group_output_row_height))
        crop_box_mask_1 = (0,
                           0,
                           graphics_constants.spritesheet_width,
                           0 + graphics_constants.spriterow_height)
        crop_box_mask_2 = (0,
                           0 + graphics_constants.spriterow_height,
                           graphics_constants.spritesheet_width,
                           0 + (2 * graphics_constants.spriterow_height))

        vehicle_mask.paste(vehicle_mask_base_image, crop_box_mask_1)
        vehicle_mask.paste(vehicle_mask_base_image, crop_box_mask_2)
        #vehicle_mask.show()
        crop_box_comp_dest_1 = (0,
                                0,
                                graphics_constants.spritesheet_width,
                                2 * graphics_constants.spriterow_height)
        vehicle_cargo_rows_image = Image.new("P", (graphics_constants.spritesheet_width, cargo_group_output_row_height))
        vehicle_cargo_rows_image.putpalette(DOS_PALETTE)
        # paste empty states in for the cargo rows (base image = empty state)
        vehicle_cargo_rows_image.paste(self.vehicle_base_image, crop_box_comp_dest_1)
        #vehicle_cargo_rows_image.show()
        crop_box_dest = (0,
                         0,
                         graphics_constants.spritesheet_width,
                         cargo_group_output_row_height)
        for cargo_labels, cargo_filenames in graphics_constants.piece_cargo_maps:
            for cargo_filename in cargo_filenames:
                cargo_sprites_input_path = os.path.join(currentdir, 'src', 'graphics', 'cargos', cargo_filename + '.png')
                cargo_sprites_input_image = Image.open(cargo_sprites_input_path)
                cargo_sprites = []
                # build a list, with a two-tuple (cargo_sprite, mask) for each of 4 angles
                # cargo sprites are assumed to be symmetrical, only 4 angles are needed
                # for cargos with 8 angles (e.g. bulldozers), provide those manually as custom cargos?
                # loading states are first 4 sprites, loaded are second 4, all in one list
                for bboxes in cargo_spritesheet_bounding_boxes[self.ship.gestalt_graphics.cargo_length]:
                    for i in bboxes:
                        cargo_sprite = cargo_sprites_input_image.copy()
                        cargo_sprite = cargo_sprite.crop(i)
                        cargo_mask = cargo_sprite.copy()
                        # !! .point is noticeably slow although not signifcantly so with only 3 cargo types
                        # !! check this again if optimisation is a concern - can cargos be processed once and passed to the pipeline?
                        cargo_mask = cargo_mask.point(lambda i: 0 if i == 0 else 255).convert("1")
                        cargo_sprites.append((cargo_sprite, cargo_mask))
                vehicle_comped_image = vehicle_cargo_rows_image.copy()
                for pixel in loc_points:
                    angle_num = 0
                    for counter, bbox in enumerate(global_constants.spritesheet_bounding_boxes):
                        if pixel[0] >= bbox[0]:
                            angle_num = counter
                    # clamp angle_num to 4, cargo sprites are symmetrical, only 4 angles provided
                    if angle_num > 3:
                        angle_num = angle_num % 4
                    cargo_sprite_num = angle_num
                    # loaded sprites are the second block of 4 in the cargo sprites list
                    if pixel[1] >= graphics_constants.spriterow_height:
                        cargo_sprite_num = cargo_sprite_num + 4
                    cargo_width = cargo_sprites[cargo_sprite_num][0].size[0]
                    cargo_height = cargo_sprites[cargo_sprite_num][0].size[1]
                    # the +1s for height adjust the crop box to include the loc point
                    # (needed beause loc points are left-bottom not left-top as per co-ordinate system, makes drawing loc points easier)
                    cargo_bounding_box = (pixel[0],
                                          pixel[1] - cargo_height + 1,
                                          pixel[0] + cargo_width,
                                          pixel[1] + 1)
                    vehicle_comped_image.paste(cargo_sprites[cargo_sprite_num][0], cargo_bounding_box, cargo_sprites[cargo_sprite_num][1])
                # vehicle overlay with mask - overlays any areas where cargo shouldn't show
                vehicle_comped_image.paste(self.vehicle_base_image, crop_box_comp_dest_1, vehicle_mask)
                #vehicle_comped_image.show()
                vehicle_comped_image_as_spritesheet = self.make_spritesheet_from_image(vehicle_comped_image)
                self.units.append(AppendToSpritesheet(vehicle_comped_image_as_spritesheet, crop_box_dest))
                self.units.append(SimpleRecolour(recolour_map=self.ship.gestalt_graphics.hull_recolour_map))

    def render(self, variant, ship, global_constants):
        self.hull_input_path = os.path.join(currentdir, 'src', 'graphics', 'hulls', ship.hull.spritesheet_name + '.png')
        self.waterline_mask_input_path = os.path.join(currentdir, 'src', 'graphics', 'waterline_masks', ship.hull.mask_name + '.png')
        self.units = []
        self.ship = ship

        crop_box_source = (0,
                           10,
                           graphics_constants.spritesheet_width,
                           10 + graphics_constants.spriterow_height)
        # create a base vehicle image by comping in hull, with empty / loading / loaded hull states
        self.vehicle_base_image = self.extend_base_image_to_3_rows_with_waterline_masked_per_load_state(Image.open(self.ship_template_input_path).crop(crop_box_source))
        # the cumulative_input_spriterow_count updates per processed group of spriterows, and is key to making this work
        cumulative_input_spriterow_count = 0
        for vehicle_counter, vehicle_rows in enumerate(ship.get_spriterow_counts()):
            self.cur_vehicle_empty_row_offset = 10 + cumulative_input_spriterow_count * graphics_constants.spriterow_height
            for spriterow_data in vehicle_rows:
                spriterow_type = spriterow_data[0]
                self.base_offset = 10 + (graphics_constants.spriterow_height * cumulative_input_spriterow_count)
                if spriterow_type == 'always_use_same_spriterow' or spriterow_type == 'empty':
                    input_spriterow_count = 1
                    self.add_generic_spriterow()
                elif spriterow_type == 'livery_only':
                    input_spriterow_count = 1
                     # specific to tankers, see notes in method about container support in future
                    self.add_livery_only_spriterows()
                elif spriterow_type == 'bulk_cargo':
                    input_spriterow_count = 2
                    self.add_bulk_cargo_spriterows()
                elif spriterow_type == 'piece_cargo':
                    input_spriterow_count = 2
                    self.add_piece_cargo_spriterows(global_constants)
                cumulative_input_spriterow_count += input_spriterow_count

        input_image = Image.open(self.ship_template_input_path).crop((0, 0, graphics_constants.spritesheet_width, 10))
        result = self.render_common(variant, ship, input_image, self.units)
        return result

def get_pipeline(pipeline_name):
    # return a pipeline by name;
    # add pipelines here when creating new ones
    for pipeline in [ExamplePassThroughPipeline(),
                     ExtendSpriterowsForCompositedCargosPipeline()]:
        if pipeline_name == pipeline.name:
            return pipeline
    raise Exception("Pipeline not found: " + pipeline_name) # should never get to here

def main():
    print("yeah, pipelines.main() does nothing")

if __name__ == '__main__':
    main()
