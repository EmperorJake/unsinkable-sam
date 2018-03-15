import global_constants
from ship import LivestockCarrier

ship = LivestockCarrier(id = 'livestock_carrier_large',
                    numeric_id = 16,
                    title = '[Livestock Carrier]',
                    subtype = 'D',
                    hull = 'ShipHouseForward',
                    buy_cost = 28,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    intro_date = 1870,
                    effect_type = 'EFFECT_SPRITE_DIESEL')

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
