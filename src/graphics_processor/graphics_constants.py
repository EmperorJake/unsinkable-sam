# colour defaults
CC1 = 198
CC2 = 80

# a convenience constant that holds a mapping for swapping CC1 and CC2 around
CC1_CC2_SWAP_MAP = {}
for i in range(8):
    CC1_CC2_SWAP_MAP[CC1 + i] = CC2 + i
    CC1_CC2_SWAP_MAP[CC2 + i] = CC1 + i

hull_recolour_CC1 = {136: CC1, 137: CC1+1, 138: CC1+2, 139: CC1+3, 140: CC1+4, 141: CC1+5, 142: CC1+6, 143: CC1+7}
hull_recolour_CC2 = {136: CC2, 137: CC2+1, 138: CC2+2, 139: CC2+3, 140: CC2+4, 141: CC2+5, 142: CC2+6, 143: CC2+7}

# facts about 'standard' spritesheets, spritesheets varying from this will be painful
spriterow_height = 100
spritesheet_top_margin = 10
spritesheet_width = 876

vehicles_input_dir = 'ships'

# --- Livery Recolour Maps ---- #
# label order matters, so tuples are used not dicts
# could probably have used orderedict or named tuple, but...blah

# keep cargos in alphabetical order for ease of reading
# DFLT label is a hack to provide specific livery for unknown cargos and should not be added to cargo translation table

# Containers
# !! simple recolouring, not cargo specific.  May need work ??  Could be cargo-specific??
container_recolour_maps = ({170 + i: CC1 + i for i in range(8)},
                           {170 + i: CC2 + i for i in range(8)},
                           {170 + i: 8 + i for i in range(8)})
# Edibles tankers, only DFLT is used as of Jan 2018
edibles_tanker_livery_recolour_maps = (# see note on DFLT above
                                      ("DFLT", {136: 5, 137: 7, 138: 8, 139: 9,
                                                140: 10, 141: 11, 142: 12, 143: 13,
                                                60: 1, 72: 3, 123: 4, 74: 5, 75: 4}),)
fruit_veg_carrier_livery_recolour_maps = (# see note on DFLT above
                                      ("DFLT", hull_recolour_CC2),)
# Livestock carrier, only DFLT is used as of Jan 2018
livestock_carrier_livery_recolour_maps = (# see note on DFLT above
                                      ("DFLT", hull_recolour_CC2),)
# Mail, only DFLT is used as of Jan 2018
mail_livery_recolour_maps = (# see note on DFLT above
                                      ("DFLT", hull_recolour_CC1),)
# Mail, only DFLT is used as of Mar 2018
pax_fast_loading_livery_recolour_maps = (# see note on DFLT above
                                      ("DFLT", hull_recolour_CC1),)
# Pax Luxury, only DFLT is used as of Mar 2018
pax_luxury_livery_recolour_maps = (# see note on DFLT above
                                      ("DFLT", hull_recolour_CC2),)
# Piece goods carrier, only DFLT is used as of Jan 2018
piece_goods_carrier_livery_recolour_maps = (# see note on DFLT above
                                      ("DFLT", hull_recolour_CC1),)
# Refrigerated ships, only DFLT is used as of Jan 2018
# !! possibly this is the same as edibles_tanker map, and could be consolidated ??
reefer_livery_recolour_maps = (# see note on DFLT above
                                      ("DFLT", {136: 5, 137: 7, 138: 8, 139: 9,
                                                140: 10, 141: 11, 142: 12, 143: 13,
                                                60: 1, 72: 3, 123: 4, 74: 5, 75: 4}),)
# Tankers
# OIL_ is in first position as the buy menu sprites should be the Oil sprites, and this is the easiest way to do it
# in principle that's wrong, because in a map without oil, the buy menu won't match the sprites of the vehicle when built
# try it and see what happens eh?
tanker_livery_recolour_maps = (("OIL_", {136: 1, 137: 2, 138: 3, 139: 4,
                                         140: 5, 141: 6, 142: 7, 143: 8}),  # see note on oil above
                               # see note on DFLT above
                               ("DFLT", {136: 198, 137: 199, 138: 200, 139: 201,
                                         140: 202, 141: 203, 142: 204, 143: 205}),
                               ("SULP", {136: 62, 137: 63, 138: 64, 139: 65,
                                         140: 66, 141: 67, 142: 68, 143: 69}),
                               ("CHLO", {136: 154, 137: 155, 138: 156, 139: 157,
                                         140: 158, 141: 159, 142: 160, 143: 161}),
                               # RFPR deliberately 2CC to allow combining with 1CC livery details
                               ("RFPR", {136: 80, 137: 81, 138: 82, 139: 83,
                                         140: 84, 141: 85, 142: 86, 143: 87}),
                               ("RUBR", {136: 40, 137: 41, 138: 42, 139: 43,
                                         140: 44, 141: 45, 142: 46, 143: 47}),
                               ("PETR", {136: 16, 137: 17, 138: 18, 139: 19,
                                         140: 20, 141: 21, 142: 22, 143: 23}))
# Trawler, only DFLT is used as of Jan 2018
trawler_livery_recolour_maps = (# see note on DFLT above
                                      ("DFLT", {136: 146, 137: 147, 138: 148, 139: 149,
                                                140: 150, 141: 151, 142: 152, 143: 153}),)

# shared global constants via Polar Fox library - import at end to make the this project's constants easier to work with
# assignments are clunky - they exist to stop pyflakes tripping on 'unused' imports
import polar_fox
bulk_cargo_recolour_maps = polar_fox.bulk_cargo_recolour_maps
piece_cargo_maps = polar_fox.piece_cargo_maps
pseudo_bulk_cargo_maps = polar_fox.pseudo_bulk_cargo_maps