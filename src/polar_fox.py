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

# chameleon templating goes faster if a cache dir is used; this specifies which dir is cache dir
chameleon_cache_dir = '.chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir = 'generated'

# this is for nml, don't need to use python path module here
graphics_path = generated_files_dir + '/graphics/'

# OpenTTD's max date
max_game_date = 5000001
