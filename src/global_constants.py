# cost constants
FIXED_RUN_COST = 500.0
FUEL_RUN_COST = 10.0

grfid = r"\55\53\53\33"

metadata = {
    "dev_thread_url": "https://www.tt-forums.net/viewtopic.php?f=26&t=75762",
    "repo_url": "https://github.com/andythenorth/unsinkable-sam",
    "docs_url": "https://grf.farm/unsinkable-sam",
}

buy_menu_sort_order_ships = [
    "pax_fast_loading",
    "pax_luxury",
    "mail_ship",
    "universal_freighter_ship",
    "universal_freighter_barge",
    "cargo_liner",
    "bulk_ship",
    "bulk_barge",
    "tanker_ship",
    "tanker_barge",
    "cryo_tanker",
    "livestock_carrier",
    "reefer",
    "edibles_tanker",
    "trawler",
]

# generalised mapping of base_id to role groups
# order is significant, of both dict and base_id lists
role_group_mapping = {
    "pax": ["pax_fast_loading", "pax_luxury"],
    "mail_utility": ["mail_ship"],
    "dry_cargo": [
        "universal_freighter_ship",
        "universal_freighter_barge",
        "cargo_liner",
        "bulk_ship",
        "bulk_barge",
    ],
    "liquid_bulk": [
        "tanker_ship",
        "tanker_barge",
        "cryo_tanker",
    ],
    "foodstuffs": [
        "reefer",
        "edibles_tanker",
    ],
    "specialist": ["livestock_carrier", "trawler"],
}

# cargo aging constant - OTTD default is 185 - dibble this up in favour of ships, as they are relatively slow
CARGO_AGE_PERIOD = 370

# spritesheet bounding boxes, each defined by a 3 tuple (left x, width, height);
# upper y is determined by spritesheet row position, so isn't defined as a constant
spritesheet_bounding_boxes = (
    (20, 28, 89),
    (60, 113, 66),
    (190, 128, 48),
    (330, 113, 66),
    (460, 28, 89),
    (500, 113, 66),
    (630, 128, 48),
    (770, 113, 66),
)

# standard vehicle offsets; custom can be supported if needed by extending ship.offsets
vehicle_offsets = {
    "32px": [
        [-14, -73],
        [-44, -38],
        [-22, -36],
        [8, -38],
        [-14, -73],
        [-42, -38],
        [-22, -36],
        [8, -38],
    ],
    "44px": [
        [-14, -73],
        [-44, -38],
        [-22, -36],
        [8, -38],
        [-14, -73],
        [-42, -38],
        [-22, -36],
        [8, -38],
    ],
    "64px": [
        [-14, -68],
        [-50, -35],
        [-32, -34],
        [3, -34],
        [-14, -68],
        [-50, -35],
        [-32, -34],
        [3, -34],
    ],
    "80px": [
        [-14, -58],
        [-59, -29],
        [-48, -36],
        [-8, -29],
        [-14, -58],
        [-61, -29],
        [-48, -36],
        [-9, -29],
    ],  # wrong, WIP
    "96px": [
        [-14, -58],
        [-59, -29],
        [-48, -36],
        [-8, -29],
        [-14, -58],
        [-61, -29],
        [-48, -36],
        [-9, -29],
    ],
    "112px": [
        [-14, -52],
        [-64, -26],
        [-56, -34],
        [-12, -25],
        [-14, -52],
        [-70, -25],
        [-56, -34],
        [-16, -25],
    ],
    "128px": [
        [-14, -46],
        [-70, -23],
        [-64, -34],
        [-18, -23],
        [-14, -46],
        [-72, -23],
        [-64, -34],
        [-18, -23],
    ],
}

buy_menu_sprite_x_loc = 970
buy_menu_sprite_width = 128
buy_menu_sprite_height = 32
sprites_max_x_extent = 885
docs_ship_image_height = (
    32  # show the full ship (assuming no ships taller than 32px in – view)
)

# shared global constants via Polar Fox library - import at end to make the this project's constants easier to work with
# done this way so we don't have to pass Polar Fox to templates, we can just pass global_constants
# assignments are clunky - they exist to stop pyflakes tripping on 'unused' imports
import polar_fox.constants

base_refits_by_class = polar_fox.constants.base_refits_by_class
cargo_labels = polar_fox.constants.cargo_labels
chameleon_cache_dir = polar_fox.constants.chameleon_cache_dir
default_cargos = polar_fox.constants.default_cargos
allowed_refits_by_label = polar_fox.constants.allowed_refits_by_label
disallowed_refits_by_label = polar_fox.constants.disallowed_refits_by_label
generated_files_dir = polar_fox.constants.generated_files_dir
graphics_path = polar_fox.constants.graphics_path
mail_multiplier = polar_fox.constants.mail_multiplier
max_game_date = polar_fox.constants.max_game_date
