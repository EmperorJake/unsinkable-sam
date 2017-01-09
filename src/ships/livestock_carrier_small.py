import global_constants
from ship import LivestockCarrier

ship = LivestockCarrier(id = 'livestock_carrier_small',
                    numeric_id = 20,
                    title = 'Small [Livestock Carrier]',
                    size_class = 'small',
                    buy_cost = 28,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    intro_date = 1870,
                    effects = ['EFFECT_SPRITE_STEAM, 8, 0, 24'])

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
