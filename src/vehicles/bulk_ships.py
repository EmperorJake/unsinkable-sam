from ship import BulkCarrier


def main():
    ship = BulkCarrier(
        id="bulk_ship_C",
        numeric_id=54,
        name="Saltlick [Mini Bulker]",
        subtype="C",
        hull="ShipHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkCarrier(
        id="bulk_ship_D",
        numeric_id=53,
        name="Lotsberget [Mini Bulker]",
        subtype="D",
        hull="ShipHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkCarrier(
        id="bulk_ship_E",
        numeric_id=51,
        name="Gravelly [Mini Bulker]",
        subtype="E",
        hull="ShipHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )

    ship = BulkCarrier(
        id="bulk_ship_F",
        numeric_id=50,
        name="Alligator [Mini Bulker]",
        subtype="F",
        hull="ShipHouseRear",
        fixed_run_cost_factor=3.5,
        fuel_run_cost_factor=1.0,
        intro_date=1870,
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
