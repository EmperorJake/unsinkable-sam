import global_constants
from ship import Tanker

ship = Tanker(id='tanker_C',
              numeric_id=1,
              title='[Tanker]',
              subtype='C',
              hull='BargeHouseRear',
              buy_cost=28,
              fixed_run_cost_factor=2.0,
              fuel_run_cost_factor=1.8,
              intro_date=1870,
              str_type_info='SMALL_TANKER_COASTAL_INLAND',
              effect_type='EFFECT_SPRITE_DIESEL')

ship.add_model_variant(intro_date=0,
                       end_date=global_constants.max_game_date,
                       spritesheet_suffix=0)
