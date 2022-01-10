# Napište a otypujte funkci ‹parse_gps›, která přečte GPS souřadnice
# ze vstupního řetězce ‹raw›. Očekávaný vstup je ve formátu
# ‹lat=X;lon=Y› kde ‹X› a ‹Y› jsou čísla s povinnou desetinnou
# tečkou. Je-li vstup ve správném formátu a obě souřadnice spadají
# do svého přípustného rozsahu, funkce vrátí dvojici hodnot typu
# ‹float›, které odpovídají číselným hodnotám zeměpisné šířky
# (latitude) a délky (longitude). V opačném případě vrátí ‹None›.
# Přípustný rozsah zeměpisné šířka je -90 až 90 a zeměpisné délky
# -180 až 180.
from typing import Tuple, Optional, List

Coords = Tuple[float, float]


def parse_gps(raw: str) -> Optional[Coords]:
    if raw.count(";") != 1:
        return None

    left, right = raw.split(";")
    if left[:4] != "lat=" and right[:4] != "lon=":
        return None

    left_num: str = left[4:]
    right_num: str = right[4:]
    if left_num.count(".") != 1 and right_num.count(".") != 1:
        return None

    # ugly af
    if (
        not left_num.split(".")[0].replace("-", "").isnumeric()
        or not left_num.split(".")[1].isnumeric()
    ):
        return None

    if (
        not right_num.split(".")[0].replace("-", "").isnumeric()
        or not right_num.split(".")[1].isnumeric()
    ):
        return None

    left_float, right_float = float(left_num), float(right_num)
    if -90 <= left_float <= 90 and -180 <= right_float <= 180:
        return left_float, right_float
    return None


# Dále napište a otypujte funkci ‹parse_gps_stream›, která přečte
# seznam GPS souřadnic a vrátí seznam dvojic s číselnými hodnotami
# souřadnic. Souřadnice na vstupu jsou každá na vlastním řádku.
# Nekóduje-li kterýkoliv řádek GPS souřadnici, funkce vrátí ‹None›.


def parse_gps_stream(raw: str) -> Optional[List[Coords]]:
    if not raw:
        return []

    result = []

    for entry in raw.split("\n"):
        parsed = parse_gps(entry)
        if parsed is None:
            return None
        result.append(parsed)
    return result


def main() -> None:
    assert parse_gps("lat=49.2099839;lon=16.5989169") == (49.2099839, 16.5989169)
    assert parse_gps("lat=49.2099839;lon=-16.5989169") == (49.2099839, -16.5989169)
    assert parse_gps("lat=-49.2099839;lon=16.5989169") == (-49.2099839, 16.5989169)

    assert parse_gps("lat=99.2099839;lon=16.5989169") is None, "latitude out of range"
    assert parse_gps("lat=-99.2099839;lon=16.5989169") is None, "latitude out of range"
    assert (
        parse_gps("lat=49.2099839;lon=-196.5989169") is None
    ), "longitude out of range"
    assert parse_gps("lat=49.2099839;lon=196.5989169") is None, "longitude out of range"
    assert parse_gps("text") is None, "invalid format"
    assert parse_gps("49.2099839;16.5989169") is None, "invalid format"
    assert parse_gps("lat=49.2099839 lon=16.5989169") is None, "invalid format"
    assert parse_gps("lon=16.5989169;lat=49.2099839") is None, "invalid format"
    assert parse_gps("lat=49;lon=16") is None, "invalid format"
    assert parse_gps("lat=49;2099839;lon=16;5989169") is None, "invalid format"
    assert parse_gps("lat=-49.2O99839;lon=16.5989l69") is None, "invalid format"

    assert (
        parse_gps_stream(
            """lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=17.1093064
lat=50.0835494;lon=14.4341414"""
        )
        == [
            (49.2099839, 16.5989169),
            (48.1516986, 17.1093064),
            (50.0835494, 14.4341414),
        ]
    )

    assert (
        parse_gps_stream(
            """lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=-17.1093064
lat=-50.0835494;lon=14.4341414"""
        )
        == [
            (49.2099839, 16.5989169),
            (48.1516986, -17.1093064),
            (-50.0835494, 14.4341414),
        ]
    )

    assert parse_gps_stream("") == []

    assert (
        parse_gps_stream(
            """lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=-189.1093064
lat=-50.0835494;lon=14.4341414"""
        )
        is None
    )

    assert (
        parse_gps_stream(
            """lat=49.2099839;lon=16.5989169
lat=48.1516986;lon=17.1093064
invalid entry"""
        )
        is None
    )


if __name__ == "__main__":
    main()
