from ship import CoveredHopperCarrier

ship = CoveredHopperCarrier(id='covered_hopper_carrier_D',
                            numeric_id=33,
                            title='[Covered Hopper Barge]',
                            subtype='D',
                            hull='PushBargeHouseRear',
                            buy_cost=28,
                            fixed_run_cost_factor=3.5,
                            fuel_run_cost_factor=1.0,
                            intro_date=1870,
                            effect_type='EFFECT_SPRITE_DIESEL')

ship.add_model_variant(spritesheet_suffix=0)
