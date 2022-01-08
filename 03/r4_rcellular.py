# Podobně jako v ‹cellular› budeme v této úloze pracovat
# s 1D buněčným automatem. Místo výpočtu nové konfigurace do
# nového seznamu ale budeme «modifikovat» stávající seznam.
#
# Toto samozřejmě nelze při použití stejných pravidel: v době
# vyhodnocování ‹i›-té buňky by již byla buňka s indexem ‹i -
# 1› přepsaná novou hodnotou. Proto použijeme pravidlo, které se
# dívá jen doprava:
#
# │‹old[i]›│‹old[i + 1]›│‹old[i + 2]›│‹new[i]›│
# ├┄┄┄┄┄┄┄┄┼┄┄┄┄┄┄┄┄┄┄┄┄┼┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄│
# │    1   │      0     │      0     │    0   │
# │    0   │      1     │      0     │    1   │
# │    0   │      1     │      1     │    1   │
# │    1   │      0     │      1     │    0   │
# │    1   │      1     │      1     │    0   │
#
# Na rozdíl od předchozích příkladů, budeme v tomto implementovat
# «proceduru»: ‹cellular_in_situ› nebude hodnotu vracet, místo toho
# bude editovat seznam, který dostala jako parametr (viz též úvod
# k tomuto týdnu).
from typing import List, Callable

# Credits: tomsko#4828

RULES = {(1, 0, 0): 0, (0, 1, 0): 1, (0, 1, 1): 1, (1, 0, 1): 0, (1, 1, 1): 0}


def cellular_in_situ2(state: List[int]) -> None:
    if not state:
        return None

    for i, cell in enumerate(zip(state, state[1:], state[2:])):
        state[i] = RULES.get(cell, state[i])

    state[-2] = RULES.get((state[-2], state[-1], 0), state[-2])
    state[-1] = RULES.get((state[-1], 0, 0), state[-1])


def cellular_in_situ1(state: List[int]) -> None:
    for i, cell in enumerate(zip(state, state[1:] + [0], state[2:] + [0, 0])):
        state[i] = RULES.get(cell, state[i])


def main(fun: Callable[[List[int]], None]) -> None:
    state = [1, 0, 0, 1, 1, 0]
    fun(state)
    assert state == [0, 0, 1, 1, 0, 0]
    fun(state)
    assert state == [0, 1, 1, 0, 0, 0]

    state = []
    fun(state)
    assert state == []

    state = [1, 1, 1, 1]
    fun(state)
    assert state == [0, 0, 1, 0]
    fun(state)
    assert state == [0, 1, 0, 0]


if __name__ == "__main__":
    main(cellular_in_situ1)
    main(cellular_in_situ2)
