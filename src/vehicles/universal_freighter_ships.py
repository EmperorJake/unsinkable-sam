from ship import UniversalFreighterShip


def main():
    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=6,
        name="Matson",
        gen=2,
        subtype="A",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=5,
        name="Gelenbeek",
        gen=2,
        subtype="B",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=4,
        name="Eagle",
        gen=2,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_STEAM",
        cargo_length=6,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=3,
        name="Akraberg",
        gen=2,
        subtype="D",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=41,
        name="Shackleton",
        gen=2,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=False,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=42,
        name="Longstone",
        gen=2,
        subtype="F",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
    )

    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=30,
        name="Thesiger",
        gen=3,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=True,
    )


"""
    ship = UniversalFreighterShip(
        roster_id="default",
        numeric_id=17,
        name="Fiennes",
        gen=4,
        subtype="E",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_AIRCRAFT_BREAKDOWN_SMOKE",
        cargo_length=8,
        sprites_complete=False,
    )
"""
