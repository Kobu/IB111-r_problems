# † Vaším úkolem je tentokrát naprogramovat tzv. „hru života“ –
# jednoduchý dvourozměrný celulární automat. Simulace běží na
# čtvercové síti, kde každá buňka je mrtvá (hodnota 0) nebo živá
# (hodnota 1). V každém kroku se přepočte hodnota všech buněk, a to
# podle toho, zda byly v předchozím kroku živé a kolik měly živých
# sousedů (z celkem osmi, tzn. včetně úhlopříčných):
#
# │  stav │ živí sousedé │ výsledek │
# ├───────┼──────────────┼──────────┤
# │  živá │          0–1 │    mrtvá │
# │  živá │          2–3 │     živá │
# │  živá │          4–8 │    mrtvá │
# │┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄│
# │ mrtvá │          0–2 │    mrtvá │
# │ mrtvá │            3 │     živá │
# │ mrtvá │          4-8 │    mrtvá │

# Příklad krátkého výpočtu:
#
#  ┌───┬───┬───┐   ┌───┬───┬───┐   ┌───┬───┬───┐
#  │   │ ○ │ ○ │   │ ○ │   │ ○ │   │   │ ○ │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │ ○ │ ○ │ ○ │ → │ ○ │   │   │ → │ ○ │   │   │
#  ├───┼───┼───┤   ├───┼───┼───┤   ├───┼───┼───┤
#  │   │ ○ │ ○ │   │ ○ │   │ ○ │   │   │ ○ │   │
#  └───┴───┴───┘   └───┴───┴───┘   └───┴───┴───┘
#
# Napište čistou funkci, která dostane jako parametry počáteční stav
# hry (jako dvourozměrný seznam nul a jedniček) a počet kroků a
# vrátí stav hry po odpovídajícím počtu kroků.
from typing import List

Cell = int
State = List[List[int]]


def get_cell(x: int, y: int, state: State) -> int:
    height = len(state)
    width = len(state[0])

    if 0 <= x < width and 0 <= y < height:
        return state[y][x]
    return 0


def apply_rule(cell: Cell, alive: int) -> int:
    return int(2 <= alive <= 3) if cell else int(alive == 3)


def count_alive(x: int, y: int, state: State) -> int:
    counter = 0

    for i in range(-1, 1 + 1):
        for j in range(-1, 1 + 1):
            if j == i == 0:
                continue
            counter += get_cell(x + j, y + i, state)
    return counter


def advance(state: State) -> State:
    height = len(state)
    width = len(state[0])

    new_state = [[0 for _ in range(width)] for _ in range(height)]

    for y, row in enumerate(state):
        for x, cell in enumerate(row):
            new_state[y][x] = apply_rule(cell, count_alive(x, y, state))
    return new_state


def life(initial: State, generations: int) -> State:
    if not initial[0]:
        return initial

    for _ in range(generations):
        initial = advance(initial)

    return initial


def main() -> None:
    assert life([[]], 1) == [[]]
    assert life([[0, 1, 1], [1, 1, 1], [0, 1, 1]], 1) == [
        [1, 0, 1],
        [1, 0, 0],
        [1, 0, 1],
    ]

    assert life([[0, 1, 1], [1, 1, 1], [0, 1, 1]], 2) == [
        [0, 1, 0],
        [1, 0, 0],
        [0, 1, 0],
    ]

    assert life([[0, 1, 1], [1, 1, 1], [0, 1, 1]], 3) == [
        [0, 0, 0],
        [1, 1, 0],
        [0, 0, 0],
    ]

    assert life([[0, 1, 1], [1, 1, 1], [0, 1, 1]], 4) == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    assert life([[0, 1, 1], [1, 1, 1], [0, 1, 1]], 5) == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    assert life([[0, 1, 1], [1, 1, 1], [0, 1, 1]], 0) == [
        [0, 1, 1],
        [1, 1, 1],
        [0, 1, 1],
    ]

    assert life([[1, 1], [1, 1]], 3) == [[1, 1], [1, 1]]

    assert life([[1, 1], [0, 1]], 1) == [[1, 1], [1, 1]]

    assert life([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 0, 1], [0, 0, 1, 1]], 5) == [
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
    ]


if __name__ == "__main__":
    main()
