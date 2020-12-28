from ship import UniversalFreighter


def main():
    ship = UniversalFreighter(
        id="universal_freighter_barge_D",
        numeric_id=46,
        name="Lindau [Freight Barge]",
        subtype="D",
        hull="BargeHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighter(
        id="universal_freighter_barge_E",
        numeric_id=47,
        name="Detroit [Freight Barge]",
        subtype="E",
        hull="PushBargeHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighter(
        id="universal_freighter_barge_F",
        numeric_id=48,
        name="Roanoke [Freight Barge]",
        subtype="F",
        hull="PushBargeHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )
