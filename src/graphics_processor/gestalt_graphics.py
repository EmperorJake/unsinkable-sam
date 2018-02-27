import graphics_processor.graphics_constants as graphics_constants
from graphics_processor import pipelines

class GestaltGraphics(object):
    # simple stub class, which is extended in sub-classes to configure:
    # - hull
    # - cargo graphics (if any)
    def __init__(self):
        # no graphics processing by default
        self.pipeline = None

    @property
    def nml_template(self):
        # over-ride in sub-classes as needed
        return 'vehicle_default.pynml'

    def _get_output_row_counts_by_type(self):
        # private method because I want to reuse it in subclasses which over-ride the public method
        # provide the number of output rows per cargo group, total row count for the group is calculated later as needed
        # uses a list of 2-tuples, not a dict as order must be preserved
        result = []
        # assume an empty state spriterow - there was an optional bool flag for this per consist but it was unused so I removed it
        result.append(('empty', 1))
        if self.bulk:
            result.append(('bulk_cargo', 2 * len(graphics_constants.bulk_cargo_recolour_maps)))
        if self.piece:
            result.append(('piece_cargo', 2 * sum([len(cargo_map[1]) for cargo_map in graphics_constants.piece_cargo_maps])))
        return result

    @property
    def num_cargo_sprite_variants(self, cargo_type=None):
        # rows can be reused across multiple cargo labels, so find uniques (assumes row nums are identical when reused across labels)
        unique_row_nums = []
        for row_nums in self.cargo_row_map.values():
            if row_nums not in unique_row_nums:
                unique_row_nums.append(row_nums)
        return sum([len(i) for i in unique_row_nums])


class GestaltGraphicsVisibleCargo(GestaltGraphics):
    # used for ship with visible cargos
    # assumes *only* pixa-generated cargos are used; subclass for all other cases
    def __init__(self, **kwargs):
        super().__init__()
        # as of Jan 2018 only one pipeline is used, but support is in place for alternative pipelines
        self.pipeline = pipelines.get_pipeline('extend_spriterows_for_composited_cargos_pipeline')
        # default hull recolour to CC1, pass param to over-ride as needed
        self.hull_recolour_map = kwargs.get('hull_recolour_map', graphics_constants.hull_recolour_CC1)
        # cargo flags
        self.bulk = kwargs.get('bulk', False)
        self.piece = kwargs.get('piece', False)
        # required if piece is set, cargo sprites are available in multiple lengths, set the most appropriate
        self.cargo_length = kwargs.get('cargo_length', None)

    @property
    def generic_rows(self):
        # map unknown cargos to sprites for some other label
        # assume that piece > input_spriterow_count, it's acceptable to show something like tarps for bulk, but not gravel for piece
        if self.piece:
            return self.cargo_row_map['DFLT']
        elif self.bulk:
            return self.cargo_row_map['GRVL']
        else:
            # shouldn't reach here, but eh,
            utils.echo_message('generic_rows hit an unknown result in GestaltGraphics')
            return [0]

    @property
    def nml_template(self):
        return 'vehicle_with_visible_cargo.pynml'

    def get_output_row_counts_by_type(self):
        return self._get_output_row_counts_by_type()

    @property
    def cargo_row_map(self):
        result = {}
        counter = 0
        if self.bulk:
            for cargo_map in graphics_constants.bulk_cargo_recolour_maps:
                result[cargo_map[0]] = [counter] # list because multiple spriterows can map to a cargo label
                counter += 1
        if self.piece:
            for cargo_labels, cargo_filenames in graphics_constants.piece_cargo_maps:
                num_variants = len(cargo_filenames)
                spriterow_nums = [counter + i for i in range(num_variants)]
                for cargo_label in cargo_labels:
                    result[cargo_label] = spriterow_nums
                counter += num_variants
        return result


class GestaltGraphicsLiveryOnly(GestaltGraphics):
    # subclass of GestaltGraphics to handle the specific case of cargos shown only by vehicle livery
    # this can also be used for recolouring hulls in the case of just a *single* livery with no visible cargo
    def __init__(self, recolour_maps, **kwargs):
        super().__init__()
        # as of Jan 2018 only one pipeline is used, but support is in place for alternative pipelines
        self.pipeline = pipelines.get_pipeline('extend_spriterows_for_composited_cargos_pipeline')
        # recolour_maps map cargo labels to liveries, use 'DFLT' as the labe in the case of just one livery
        self.recolour_maps = recolour_maps

    @property
    def generic_rows(self):
        utils.echo_message ('generic_rows not implemented in GestaltGraphicsLiveryOnly')
        return None

    @property
    def nml_template(self):
        return 'vehicle_with_cargo_specific_liveries.pynml'

    def get_output_row_counts_by_type(self):
        # the template for visible livery requires the count of _all_ the liveries, *no calculating later*
        # 3 rows per livery (empty, 50% load, 100% load)
        return [('livery_only', 3 * self.num_cargo_sprite_variants)]

    @property
    def cargo_row_map(self):
        # !! this works more by accident than design
        # !! the order of cargo types here must be kept in sync with the order in the cargo graphics processor
        result = {}
        counter = 0
        for cargo_map in self.recolour_maps:
            result[cargo_map[0]] = [counter] # list because multiple spriterows can map to a cargo label
            counter += 1
        return result


class GestaltGraphicsCustom(GestaltGraphics):
    # Subclass of GestaltGraphics to handle cases like vehicles with hand-drawn cargo (no generation).
    # this cannot currently also use pixa-generated cargos
    # - pixa cargo pipeline has no support for compositing custom rows, that looked like TMWFTLB
    def __init__(self, _cargo_row_map, _nml_template, generic_rows):
        super().__init__()
        # as of Jan 2018 only one pipeline is used, but support is in place for alternative pipelines
        self.pipeline = pipelines.get_pipeline('extend_spriterows_for_composited_cargos_pipeline')
        # options
        self.custom = True
        self._nml_template = _nml_template
        self._cargo_row_map = _cargo_row_map
        self._generic_rows = generic_rows

    @property
    def generic_rows(self):
        # generic rows is normally automated, but for custom, get it from a manully specified property
        return self._generic_rows

    @property
    def nml_template(self):
        return self._nml_template

    def get_output_row_counts_by_type(self):
        # assume we want whatever the base class count of rows is (handles empty state etc)
        # ^ that might not be viable as it ties 'custom' to same template assumptions as base class - change if needed eh?
        result = self._get_output_row_counts_by_type()
        # assume two output rows (loading, loaded) - extend this if it's not viable
        result.append(('custom_cargo', 2))
        return result

    @property
    def cargo_row_map(self):
        return self._cargo_row_map
