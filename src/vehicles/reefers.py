from ship import Reefer


def main():
    ship = Reefer(
        numeric_id=61,
        name="Langara",
        gen=2,
        subtype="B",
        hull="BargeHouseRear",
        effect_type="EFFECT_SPRITE_DIESEL",
        cargo_length=3,
    )

    ship = Reefer(
        numeric_id=60,
        name="Samphire",
        gen=2,
        subtype="C",
        hull="ShipHouseRear",
        effect_type="EFFECT_SPRITE_STEAM",
        cargo_length=6,
    )

    ship = Reefer(
        numeric_id=14,
        name="Kodiak",
        gen=2,
        subtype="D",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Reefer(
        numeric_id=59,
        name="Caribou",
        gen=2,
        subtype="E",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_STEAM",
    )

    ship = Reefer(
        numeric_id=15,
        name="Helsinki",
        gen=2,
        subtype="F",
        hull="ShipHouseForward",
        effect_type="EFFECT_SPRITE_DIESEL",
        sprites_complete=False,
    )
