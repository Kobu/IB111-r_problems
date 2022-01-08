# † Naprogramujte proceduru ‹partition›, která na vstup dostane
# seznam čísel ‹data› a platný index ‹idx›. Pro pohodlnost hodnotu
# ‹data[idx]› nazveme ‹pivot›.
#
# Procedura přeuspořádá seznam tak, že přesune prvky menší než
# ‹pivot› před ‹pivot› a prvky větší než ‹pivot› za ‹pivot›.
#
# Po transformaci bude tedy seznam «pomyslně» rozdělen na tři části:
#
#   • čísla menší než ‹pivot›
#   • pivot
#   • čísla větší než ‹pivot›
#
# Relativní pořadí prvků v první a poslední části není definováno,
# takže oba následovné výsledky pro seznam ‹[3, 4, 1, 2, 0]› a index
# ‹0› jsou správné: ‹[1, 0, 2, 3, 4]› nebo ‹[1, 2, 0, 3, 4]›.

# Při řešení nepoužívejte zabudované funkce pro řazení (funkce
# ‹partition› je mimo jiné pomocná funkce algoritmu quicksort, bylo
# by tedy absurdní zde sekvenci celou řadit).
from typing import List, Set


# Credits: mm_stanone#3636, tomsko#4828


def is_sorted(data: List[int], idx: int) -> bool:
    return all(x < data[idx] for x in data[:idx]) and all(
        x > data[idx] for x in data[idx:]
    )


def partition(data: List[int], idx: int) -> None:
    pivot = data[idx]

    cursor_left = 0
    cursor_right = len(data) - 1

    while cursor_right != cursor_left:
        while data[cursor_left] < pivot and cursor_left <= idx:
            cursor_left += 1

        while data[cursor_right] > pivot and cursor_right >= idx:
            cursor_right -= 1

        if cursor_right == cursor_left == idx:
            return None

        elif cursor_left != idx and cursor_right != idx:
            data[cursor_left], data[cursor_right] = (
                data[cursor_right],
                data[cursor_left],
            )

        elif cursor_left == idx:
            data[cursor_right], data[idx] = data[idx], data[cursor_right]
            idx = cursor_right

        elif cursor_right == idx:
            data[cursor_left], data[idx] = data[idx], data[cursor_left]
            idx = cursor_left


def main() -> None:
    # Datový typ ‹set› používáme, abychom ze seznamu vytvořili
    # množinu – potřebujeme se vypořádat s neurčitostí pořadí prvků
    # v prefixu resp. sufixu po volání procedury ‹partition›. O typu
    # ‹set› se více dozvíte později.

    run_test([3, 4, 6, 2, 5], 4, {2, 3, 4}, {6})
    run_test([0, 1, 3, 4, 6, 2, 5], 4, {0, 1, 3, 4, 5, 2}, set([]))
    run_test([0, 1, 3, 4, 6, 2, 5], 2, {0, 1, 2}, {4, 5, 6})
    run_test([0, 2, 1, 5, 6, 9], 0, set([]), {2, 1, 5, 6, 9})
    run_test([0, 2, 1, 5, 6, 9], 3, {0, 1, 2}, {6, 9})
    run_test([6, 9, 3, 0, 1], 2, {0, 1}, {6, 9})


def run_test(data: List[int], idx: int, prefix: Set[int], postfix: Set[int]) -> None:
    pivot = data[idx]
    partition(data, idx)
    assert set(data[: len(prefix)]) == prefix
    assert data[len(prefix)] == pivot
    assert set(data[len(prefix) + 1 :]) == postfix


if __name__ == "__main__":
    main()
