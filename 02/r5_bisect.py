# † Napište funkci ‹bisect›, která aproximuje kořen spojité funkce
# ⟦f⟧ (předané parametrem ‹fun›) s chybou menší než ‹epsilon› na
# zadaném intervalu od ‹low› po ‹high› včetně. Algoritmus bisekce
# předpokládá, že v zadaném intervalu se nachází právě jedno řešení.
#
# Při hledání řešení postupujte následovně:
#
#  1. spočtěte hodnotu funkce pro bod uprostřed intervalu, a je-li
#     výsledek v rozsahu povolené chyby, vraťte tento bod,
#  2. jinak spočtěte hodnoty funkce v hraničních bodech intervalu
#     a zjistěte, ve které polovině má funkce kořen,
#  3. opakujte výpočet s vybranou polovinou jako s novým intervalem.
#
# Chybu ⟦e⟧ spočtete v bodě ⟦x⟧ jako ⟦e = |f(x)|⟧.
#
# Poznámka: funkci předanou parametrem můžete v Pythonu normálně
# volat jako libovolnou jinou funkci.

from typing import Callable
from math import sqrt


# Credits: bobtheskrob#8192


def bisect1(
    fun: Callable[[float], float], low: float, high: float, eps: float
) -> float:
    midpoint = (low + high) / 2
    midpoint_res = abs(fun(midpoint))

    if midpoint_res < eps:
        return midpoint

    left, right = abs(fun(low)), abs(fun(high))

    if left > right:
        return bisect1(fun, midpoint, high, eps)
    return bisect1(fun, low, midpoint, eps)


def bisect2(
    fun: Callable[[float], float], low: float, high: float, eps: float
) -> float:
    mid = (low + high) / 2

    while abs(fun(mid)) > eps:
        mid = (low + high) / 2

        if abs(fun(low)) > abs(fun(high)):
            low = mid
        else:
            high = mid

    return mid


def fun_a(x: float) -> float:
    return x ** 2 - 3


def fun_b(x: float) -> float:
    return x ** 3 - x - 1


def fun_c(x: float) -> float:
    return sqrt(x) / x - x ** 3 + 5


def main(
    bisect: Callable[[Callable[[float], float], float, float, float], float]
) -> None:
    assert abs(fun_a(bisect(fun_a, 1, 2, 0.01))) < 0.01
    assert abs(fun_a(bisect(fun_a, 1, 2, 0.0001))) < 0.0001
    assert abs(fun_b(bisect(fun_b, 1, 5, 0.001))) < 0.001
    assert abs(fun_c(bisect(fun_c, 1, 10, 0.001))) < 0.001


if __name__ == "__main__":
    main(bisect1)
    main(bisect2)
