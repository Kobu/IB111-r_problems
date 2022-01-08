# Napište (čistou) funkci, která jako parametr dostane seznam
# obdélníků a vrátí seznam obdélníků, které se překrývají s nějakým
# jiným. Obdélník samotný je reprezentovaný dvěma body (levým dolním
# a pravým horním rohem, a má nenulovou výšku i šířku). Obdélníky
# budeme zapisovat jako dvojice dvojic – ‹((0, 0), (1, 2))›
# například reprezentuje tento obdélník:
#
#           ┌───┐(1, 2)
#           │   │
#           │   │
#     (0, 0)└───┘
#
# Mohl by se Vám hodit predikát, který je pravdivý, když se dva
# obdélníky překrývají:
from typing import Tuple, List

# Credits: adames4#1754

Point = Tuple[int, int]
Rectangle = Tuple[Point, Point]


def has_overlap(a: Rectangle, b: Rectangle) -> bool:
    (ax1, ay1), (ax2, ay2) = a
    (bx1, by1), (bx2, by2) = b

    return (ax1 - bx2) * (ax2 - bx1) <= 0 and (ay1 - by2) * (ay2 - by1) <= 0


def filter_overlapping(rectangles: List[Rectangle]) -> List[Rectangle]:
    result = []

    for i in range(len(rectangles)):
        for j in range(len(rectangles)):
            if i != j and has_overlap(rectangles[i], rectangles[j]):
                result.append(rectangles[i])
                break
    return result


def main() -> None:
    r1 = ((1, 1), (2, 2))
    r2 = ((0, 0), (2, 2))
    r3 = ((-2, -2), (-1, -1))
    r4 = ((10, 15), (25, 35))

    assert filter_overlapping([]) == []
    assert filter_overlapping([r1]) == []
    assert filter_overlapping([r1, r1]) == [r1, r1]
    assert filter_overlapping([r1, r2]) == [r1, r2]
    assert filter_overlapping([r2, r1]) == [r2, r1]

    assert filter_overlapping([r3, r2, r1, r4]) == [r2, r1]
    assert filter_overlapping([r2, ((1, 10), (10, 20))]) == []
    assert filter_overlapping([((15, 0), (17, 8)), ((1, 10), (10, 20))]) == []
    l2 = [((0, 0), (2, 2)), ((1, 1), (10, 10)), ((9, 9), (11, 11))]
    assert filter_overlapping(l2) == l2


if __name__ == "__main__":
    main()
