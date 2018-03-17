from ship import UniversalFreighter

ship = UniversalFreighter(id='universal_freighter_B',
                          numeric_id=5,
                          title='[Freighter]',
                          subtype='B',
                          hull='BargeHouseRear',
                          buy_cost=28,
                          fixed_run_cost_factor=3.5,
                          fuel_run_cost_factor=1.0,
                          intro_date=1870,
                          effect_type='EFFECT_SPRITE_DIESEL')

ship.add_model_variant(spritesheet_suffix=0)
