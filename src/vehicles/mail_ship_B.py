import global_constants
from ship import MailShip

ship = MailShip(id='mail_ship_B',
                numeric_id=27,
                title='[Mail Ship]',
                subtype='B',
                hull='TempHouseNone',
                buy_cost=28,
                fixed_run_cost_factor=3.5,
                fuel_run_cost_factor=1.0,
                intro_date=1870,
                effect_type='EFFECT_SPRITE_STEAM')

ship.add_model_variant(spritesheet_suffix=0)
