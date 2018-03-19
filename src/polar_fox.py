"""
This file is generated from the Polar Fox project.
Don't make changes here, make them in the Polar Fox project and redistribute.
Any changes made here are liable to be over-written.
"""

# used to construct the cargo table automatically
# ! order is significant ! - openttd will cascade through default cargos in the order specified by the cargo table
cargo_labels = ['PASS', # pax first
                'TOUR',
                # "the mail must get through"
                'MAIL',
                # all other cargos - append new ones to end, don't change order
                'COAL',
                'IORE',
                'GRVL',
                'SAND',
                'AORE',
                'CORE',
                'CLAY',
                'SCMT',
                'WOOD',
                'LIME',
                'GOOD',
                'FOOD',
                'STEL',
                'FMSP',
                'ENSP',
                'BEER',
                'BDMT',
                'MNSP',
                'PAPR',
                'WDPR',
                'VEHI',
                'COPR',
                'DYES',
                'OIL_',
                'RFPR',
                'PETR',
                'PLAS',
                'WATR',
                'FISH',
                'CERE',
                'FICR',
                'FRVG',
                'FRUT',
                'GRAI',
                'LVST',
                'MAIZ',
                'MILK',
                'RUBR',
                'SGBT',
                'SGCN',
                'WHEA',
                'WOOL',
                'OLSD',
                'SUGR',
                'JAVA',
                'BEAN',
                'NITR',
                'VEHI',
                'EOIL',
                'NUTS',
                'CASS',
                'MNO2',
                'PHOS',
                'POTA',
                'PORE',
                'IRON',
                'NICK',
                'SLAG',
                'QLME',
                'BOOM',
                'METL',
                'SULP',
                'SASH',
                'CMNT',
                'COKE',
                'KAOL',
                'FERT',
                'PIPE',
                'SALT',
                'CBLK',
                'CHLO',
                'VPTS',
                'ACID',
                'ALUM',
                'CTCD',
                'TOFF',
                'URAN',
                #
                'NULL']

# shared lists of allowed classes, shared across multiple vehicle types
base_refits_by_class = {'empty': [],
                        'all_freight': ['CC_BULK', 'CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_LIQUID', 'CC_ARMOURED', 'CC_REFRIGERATED', 'CC_COVERED', 'CC_NON_POURABLE'],
                        'pax': ['CC_PASSENGERS'],
                        'mail': ['CC_MAIL'],
                        'liquids': ['CC_LIQUID'],
                        'packaged_freight': ['CC_PIECE_GOODS', 'CC_EXPRESS', 'CC_ARMOURED', 'CC_LIQUID'],
                        'flatbed_freight': ['CC_PIECE_GOODS'],
                        'dump_freight': ['CC_BULK'],
                        'covered_hopper_freight': [], # explicit allowal by label instead
                        'refrigerated_freight': ['CC_REFRIGERATED'],
                        'express_freight': ['CC_EXPRESS','CC_ARMOURED']}

# rather than using disallowed classes (can cause breakage), specific labels are disallowed
disallowed_refits_by_label = {'non_dump_bulk': ['WOOD', 'SGCN', 'FICR', 'BDMT', 'WDPR', 'GRAI', 'WHEA', 'CERE', 'MAIZ', 'FRUT', 'BEAN', 'CMNT', 'CTCD', 'FERT', 'OLSD', 'SUGR', 'SULP', 'TOFF', 'URAN'],
                              'edible_liquids': ['MILK', 'WATR', 'BEER', 'FOOD', 'EOIL'],
                              'non_edible_liquids': ['RFPR', 'OIL_', 'FMSP', 'PETR', 'RUBR', 'SULP'],
                              'non_flatbed_freight': ['FOOD', 'FISH', 'LVST', 'FRUT', 'BEER', 'MILK', 'JAVA', 'SUGR', 'NUTS', 'EOIL', 'BOOM', 'FERT'],
                              'non_freight_special_cases': ['TOUR']}

# cascading lists of default cargos, if the first cargo(s) are not available, all will be tried in order
# avoids an issue where default cargo was weird for, e.g. some FIRS economies
# don't conflate this with general refittability, they're different concerns ;)
# vehicle classes can also just provide their own list locally, using this is convenient, not obligatory
default_cargos = {'box': ['GOOD', 'VPTS', 'FOOD'],
                  'covered_hopper': ['GRAI', 'KAOL'],
                  'dump': ['IORE', 'MNO2', 'NITR'],
                  'edibles_tank': ['WATR', 'MILK', 'BEER'],
                  'flat': ['STEL', 'COPR', 'METL'],
                  'fruit_veg': ['FRUT', 'BEAN', 'CASS', 'JAVA', 'NUTS'],
                  'hopper': ['COAL', 'CORE', 'PORE'],
                  'intermodal': ['GOOD', 'VPTS', 'FOOD'],
                  'silo': ['CMNT', 'BDMT', 'RFPR', 'QLME', 'FMSP'],
                  'stake': ['WOOD'],
                  'mail': ['MAIL'],
                  'metal': ['STEL', 'COPR'],
                  'open': ['GOOD'],
                  'pax': ['PASS'],
                  'reefer': ['FOOD'],
                  'supplies': ['ENSP'],
                  'tank': ['OIL_', 'KAOL', 'RUBR'],

                  }




# chameleon templating goes faster if a cache dir is used; this specifies which dir is cache dir
chameleon_cache_dir = '.chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir = 'generated'

# this is for nml, don't need to use python path module here
graphics_path = generated_files_dir + '/graphics/'

# OpenTTD's max date
max_game_date = 5000001

# mailbags are < 1t, multiply capacity appropriately
mail_multiplier = 2

# Graphics Constants
# ------------------

# Bulk
# keep cargos in alphabetical order for ease of reading
# SCMT *is* bulk cargo in this set, realism is not relevant here, went back and forth on this a few times :P
bulk_cargo_recolour_maps = (("AORE", {170: 42, 171: 123, 172: 74, 173: 125, 174: 162, 175: 126, 176: 78}),
                            ("CASS", {170: 53, 171: 54, 172: 55, 173: 56, 174: 57, 175: 58, 176: 59}),
                            ("CLAY", {170: 55, 171: 56, 172: 57, 173: 77, 174: 78, 175: 79, 176: 80}),
                            ("COAL", {170: 1, 171: 1, 172: 2, 173: 2, 174: 3, 175: 4, 176: 5}),
                            ("CORE", {170: 1, 171: 32, 172: 25, 173: 27, 174: 34, 175: 56, 176: 59}),
                            ("GRVL", {170: 6, 171: 4, 172: 7, 173: 8, 174: 21, 175: 11, 176: 12}),
                            ("IORE", {170: 75, 171: 76, 172: 123, 173: 122, 174: 124, 175: 74, 176: 104}),
                            ("LIME", {170: 6, 171: 4, 172: 7, 173: 8, 174: 21, 175: 11, 176: 12}),
                            ("MNO2", {170: 1, 171: 16, 172: 3, 173: 17, 174: 18, 175: 19, 176: 20}),
                            ("NITR", {170: 37, 171: 38, 172: 38, 173: 39, 174: 39, 175: 69, 176: 69}),
                            ("PHOS", {170: 63, 171: 64, 172: 192, 173: 65, 174: 193, 175: 64, 176: 194}),
                            ("PORE", {170: 40, 171: 72, 172: 73, 173: 33, 174: 33, 175: 63, 176: 63}),
                            ("POTA", {170: 63, 171: 64, 172: 192, 173: 65, 174: 193, 175: 64, 176: 194}),
                            ("SAND", {170: 108, 171: 64, 172: 65, 173: 197, 174: 36, 175: 196, 176: 197}),
                            ("SCMT", {170: 104, 171: 3, 172: 2, 173: 70, 174: 71, 175: 72, 176: 3}),
                            ("SGBT", {170: 60, 171: 53, 172: 54, 173: 55, 174: 56, 175: 57, 176: 58}))

# Piece
# 2-tuples, containing 2 lists (['LBL1', 'LBL2'], ['filename_1', 'filename_2'])
# this groups labels and sprites, but there's no obvious problem with that right now
# if a label can't share a group of sprites, it can repeat some filenames, that's just inefficient, but works
# DFLT label is a hack to support cargos with no specific sprites (including unknown cargos), and should not be added to cargo translation table
piece_cargo_maps = ((['DFLT'], ['tarps_2cc_1']),  # see note on DFLT above
                    (['BEER', 'DYES', 'EOIL', 'MILK', 'OIL_',
                      'PETR', 'RFPR', 'WATR'], ['barrels_silver']),
                    (['BDMT', ], ['tarps_red_1']),
                    (['COPR'], ['copper_coils']),
                    (['ENSP', ], ['tarps_gold_1']),
                    (['FMSP'], ['tarps_blue_1']),
                    (['GOOD'], ['crates_1']),
                    (['PAPR'], ['paper_coils']),
                    (['STEL'], ['steel_coils']),
                    (['WDPR'], ['lumber_planks']),
                    (['WOOD'], ['logs']))

# NEEDS REFACTORING EH?
# some 'bulk' cargos are better implemented as piece, as the bulk recolouring method isn't appropriate
# !! it's likely that separate maps for supplies are also needed (supplies cars don't need all piece cargos), also logs/pipes?
# !! rename as piece_open, piece_stakes, piece_supplies, piece_flat?  Or piece_rolls, piece_flows, piece_bulky, piece_simple?
pseudo_bulk_cargo_maps = ((['FRUT'], ['fruit']),
                          (['JAVA'], ['coffee']),
                          (['NUTS'], ['nuts']))

# Tanker recolour maps
# DFLT label is a hack to support cargos with no specific sprites (including unknown cargos), and should not be added to cargo translation table
tanker_livery_recolour_maps = (("OIL_", {136: 1, 137: 2, 138: 3, 139: 4,
                                         140: 5, 141: 6, 142: 7, 143: 8}),
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
