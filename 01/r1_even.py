# Uvažujme posloupnost ⟦aᵢ⟧ druhých mocnin sudých čísel ⟦aᵢ = 4i²⟧. Napište
# funkci, která vrátí sumu prvních ‹n› členů této posloupnosti ⟦sₙ = ∑ᵢ₌₁ⁿ aᵢ =
# ∑ᵢ₌₁ⁿ 4i²⟧.
from typing import Callable


def even(n: int) -> int:
    if n == 0:
        return 0

    return 4 * n ** 2 + even(n - 1)


def even2(n: int) -> int:
    res = 0
    for i in range(n + 1):
        res += 4 * i ** 2
    return res


def main(fun: Callable[[int], int]) -> None:
    assert fun(1) == 4
    assert fun(2) == 20
    assert fun(3) == 56
    assert fun(4) == 120
    assert fun(10) == 1540
    assert fun(134) == 3244140


if __name__ == "__main__":
    main(even)
    main(even2)
