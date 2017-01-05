import global_constants
from ship import UniversalFreighter

ship = UniversalFreighter(id = 'universal_freighter_large',
            numeric_id = 3,
            title = 'Large [Freighter]',
            size_class = 'large',
            capacity_cargo_holds = 576,
            buy_cost = 28,
            fixed_run_cost_factor = 3.5,
            fuel_run_cost_factor = 1.0,
            offsets = [[-15, -38], [-79, -21], [-66, -25], [-38, -22], [-14, -36], [-78, -22], [-68, -25], [-38, -20]],
            intro_date = 1870,
            buy_menu_bb_xy = [620, 28],
            effects = ['EFFECT_SPRITE_STEAM, 8, 0, 24'])

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
