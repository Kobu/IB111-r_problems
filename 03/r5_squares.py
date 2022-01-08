# Napište čistou funkci ‹least_squares›, která dostane na vstupu dva
# stejně dlouhé seznamy čísel. Hodnoty na odpovídajících pozicích
# v těchto seznamech udávají souřadnice jednoho vstupního bodu.
#
# Výsledkem funkce nechť je trojice ⟦(α, β, r)⟧ kde ⟦y = α + βx⟧
# udává přímku, která nejlépe aproximuje zadané body, a ⟦r⟧ je seznam
# tzv. residuí (vertikálních vzdáleností jednotlivých bodů od
# vypočtené přímky). Označíme-li souřadnice jednotlivých bodů ⟦(xᵢ,
# yᵢ)⟧ a ⟦x̄⟧, ⟦ȳ⟧ aritmetické průměry příslušných seznamů,
# hledané koeficienty získáte použitím těchto vzorců:

# ⟦ βₛ = ∑ ( xᵢ - x̄ )( yᵢ - ȳ )
#   βₓ = ∑ ( xᵢ - x̄ )²
#   β  = βₛ / βₓ
#   α  = ȳ - βx̄ ⟧

# V případě, že body leží na vertikální přímce (a tedy ⟦β⟧ není
# definovaná), vraťte místo trojice hodnotu ‹None›.
from typing import List, Tuple, Optional

Result = Tuple[float, float, List[float]]


def calc_beta_s(x1: float, avg_x: float, y1: float, avg_y: float) -> float:
    return (x1 - avg_x) * (y1 - avg_y)


def calc_beta_x(x1: float, avg_x: float) -> float:
    return (x1 - avg_x) ** 2


def calc_beta(beta_s: float, beta_x: float) -> float:
    return beta_s / beta_x


def calc_a(avg_y: float, beta: float, avg_x: float) -> float:
    return avg_y - beta * avg_x


def calc_vert(a: float, beta: float, x: float, y: float) -> float:
    return abs((a + beta * x) - y)


def least_squares(x: List[int], y: List[int]) -> Optional[Result]:
    avg_x = sum(x) / len(x)
    avg_y = sum(y) / len(y)

    beta_s: float = 0
    beta_x: float = 0

    for (x1, y1) in zip(x, y):
        beta_s += calc_beta_s(x1, avg_x, y1, avg_y)
        beta_x += calc_beta_x(x1, avg_x)

    if beta_x == 0:
        return None

    beta = calc_beta(beta_s, beta_x)
    a = calc_a(avg_y, beta, avg_x)

    residuals = [calc_vert(a, beta, x1, y1) for x1, y1 in zip(x, y)]

    return a, beta, residuals


def main() -> None:
    assert check([1, 2], [3, 4], (2, 1, [0, 0]))
    assert check([1, 2, 3], [3, 4, 5], (2, 1, [0, 0, 0]))
    assert least_squares([1, 1, 1], [3, 4, 5]) is None
    assert check([1, 2, 3], [2, 2, 2], (2, 0, [0, 0, 0]))
    assert check([1, 2, 3], [1, 4, 1], (2, 0, [1, 2, 1]))
    assert check([1, 2, 3], [1, 2, 4], (-2 / 3, 3 / 2, [1 / 6, 1 / 3, 1 / 6]))


def check(x: List[int], y: List[int], expect: Result) -> bool:
    from math import isclose

    res = least_squares(x, y)
    assert res and expect
    (alpha1, beta1, r1) = res
    (alpha2, beta2, r2) = expect
    if not isclose(alpha1, alpha2) or not isclose(beta1, beta2):
        return False
    for a, b in zip(r1, r2):
        if not isclose(a, b):
            return False
    return True


if __name__ == "__main__":
    main()
