import global_constants
from ship import PaxLuxuryShip

ship = PaxLuxuryShip(id = 'pax_luxury_large',
                    numeric_id = 22,
                    title = 'Large [Pax Luxury]',
                    hull = 'LargeShipHouseForward',
                    buy_cost = 28,
                    fixed_run_cost_factor = 3.5,
                    fuel_run_cost_factor = 1.0,
                    intro_date = 1870,
                    effects = ['EFFECT_SPRITE_STEAM, 8, 0, 24'])

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
