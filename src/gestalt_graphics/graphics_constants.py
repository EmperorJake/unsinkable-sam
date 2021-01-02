# colour defaults
CC1 = 198
CC2 = 80

hull_recolour_CC1 = {
    136: CC1,
    137: CC1 + 1,
    138: CC1 + 2,
    139: CC1 + 3,
    140: CC1 + 4,
    141: CC1 + 5,
    142: CC1 + 6,
    143: CC1 + 7,
}
hull_recolour_CC2 = {
    136: CC2,
    137: CC2 + 1,
    138: CC2 + 2,
    139: CC2 + 3,
    140: CC2 + 4,
    141: CC2 + 5,
    142: CC2 + 6,
    143: CC2 + 7,
}

# facts about 'standard' spritesheets, spritesheets varying from this will be painful
spriterow_height = 100
spritesheet_top_margin = 10
spritesheet_width = 1200

# --- Livery Recolour Maps ---- #
# label order matters, so tuples are used not dicts
# could probably have used orderedict or named tuple, but...blah

# keep cargos in alphabetical order for ease of reading
# DFLT label is a hack to provide specific livery for unknown cargos and should not be added to cargo translation table

# Containers
# !! simple recolouring, not cargo specific.  May need work ??  Could be cargo-specific??
container_recolour_maps = (
    {170 + i: CC1 + i for i in range(8)},
    {170 + i: CC2 + i for i in range(8)},
    {170 + i: 8 + i for i in range(8)},
)
# Livestock carrier, only DFLT is used as of Jan 2018
covered_hopper_carrier_livery_recolour_maps = (  # see note on DFLT above
    ("DFLT", hull_recolour_CC2),
)
# Gas (cryo) tankers, only DFLT is used as of Nov 2020
cryo_tanker_livery_recolour_maps = (  # see note on DFLT above
    ("DFLT", hull_recolour_CC1),
)
# Edibles tankers, only DFLT is used as of Jan 2018
edibles_tanker_livery_recolour_maps = (  # see note on DFLT above
    (
        "DFLT",
        {
            # hull
            136: 5,
            137: 7,
            138: 8,
            139: 9,
            140: 10,
            141: 11,
            142: 12,
            143: 13,
            # deck recolour
            70: 1,
            60: 2,
            72: 3,
            123: 4,
            74: 5,
            75: 6,
        },
    ),
)
fruit_veg_carrier_livery_recolour_maps = (  # see note on DFLT above
    ("DFLT", hull_recolour_CC2),
)
# Livestock carrier, only DFLT is used as of Jan 2018
livestock_carrier_livery_recolour_maps = (  # see note on DFLT above
    ("DFLT", hull_recolour_CC2),
)
# Mail, only DFLT is used as of Jan 2018
mail_livery_recolour_maps = (("DFLT", hull_recolour_CC1),)  # see note on DFLT above
# Mail, only DFLT is used as of Mar 2018
pax_fast_loading_livery_recolour_maps = (  # see note on DFLT above
    ("DFLT", hull_recolour_CC1),
)
# Pax Luxury, only DFLT is used as of Mar 2018
pax_luxury_livery_recolour_maps = (  # see note on DFLT above
    ("DFLT", hull_recolour_CC2),
)
# Piece goods carrier, only DFLT is used as of Jan 2018
piece_goods_carrier_livery_recolour_maps = (  # see note on DFLT above
    ("DFLT", hull_recolour_CC1),
)
# Refrigerated ships, only DFLT is used as of Jan 2018
# !! possibly this is the same as edibles_tanker map, and could be consolidated ??
reefer_livery_recolour_maps = (  # see note on DFLT above
    (
        "DFLT",
        {
            136: 5,
            137: 7,
            138: 8,
            139: 9,
            140: 10,
            141: 11,
            142: 12,
            143: 13,
            # deck recolour
            70: 1,
            60: 2,
            72: 3,
            123: 4,
            74: 5,
            75: 6,
        },
    ),
)
# tanker hull colours come from Polar Fox, but ship deck colour remap is local to Sam
# this one is just a simple dict which the Polar Fox remaps are extended with
tanker_deck_recolour_maps = {
    170: 17,
    171: 18,
    172: 19,
    173: 20,
    174: 21,
    175: 22,
    176: 23,
    70: 40,
    60: 41,
    72: 42,
    123: 43,
    74: 44,
    75: 45,
}
# Trawler, only DFLT is used as of Jan 2018
trawler_livery_recolour_maps = (  # see note on DFLT above
    (
        "DFLT",
        {
            136: 146,
            137: 147,
            138: 148,
            139: 149,
            140: 150,
            141: 151,
            142: 152,
            143: 153,
        },
    ),
)
