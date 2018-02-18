import global_constants
from ship import UniversalFreighter

ship = UniversalFreighter(id = 'universal_freighter_large',
                    numeric_id = 3,
                    title = 'Large [Freighter]',
                    hull = 'LargeShipHouseRear',
                    buy_cost = 28,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    intro_date = 1870,
                    effect_type = 'EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE')

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0,
                       graphics_processor=ship.graphics_processors[0])
