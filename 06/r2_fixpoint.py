from typing import Set

# Mějme funkci ‹f›, která pro dané celé číslo ‹a› vrátí množinu
# obsahující ‹a›, ‹a // 2› a ‹a // 7›. Použitím této funkce na
# množině pak míníme její použití na každém prvku dané množiny a
# následné sjednocení všech obdržených výsledků.

# Napište (čistou) funkci, která na množinu ze svého argumentu
# použije ‹f›, dále použije ‹f› na obdržený výsledek a takto bude
# pokračovat až dojde do bodu, kdy se dalším použitím ‹f› daná
# množina už nezmění. Výsledkem bude počet aplikací ‹f› na množinu,
# které bylo potřeba provést, než se proces zastavil.

# Například z množiny ‹{1, 5, 6}› vznikne první aplikací popsané
# funkce množina ‹{0, 1, 2, 3, 5, 6}›:
#
#  • hodnota ‹1› se zobrazila na ‹{1, 1 // 2 = 0, 1 // 7 = 0}›,
#  • hodnota ‹5› na ‹{5, 5 // 2 = 2, 5 // 7 = 0}›, a konečně
#  • hodnota ‹6› na ‹{6, 6 // 2 = 3, 6 // 7 = 0}›.
#
# Po další aplikaci se už množina nijak nezmění, proto je výsledkem
# číslo jedna.
from typing import Set


def f(a_set: Set[int]) -> Set[int]:
    return set.union(*[{a, a // 2, a // 7} for a in a_set])


# iterative
def fixpoint2(starting_set: Set[int]) -> int:
    if not starting_set:
        return 0

    curr_len = len(starting_set)
    new_set = f(starting_set)
    iters = 0

    while curr_len != len(new_set):
        curr_len = len(new_set)
        new_set = f(new_set)
        iters += 1

    return iters


# recursive
def fixpoint(starting_set: Set[int]) -> int:
    if not starting_set:
        return 0

    return fixpoint_rec(starting_set, 0)


def fixpoint_rec(starting_set: Set[int], iters: int) -> int:
    curr_len = len(starting_set)
    new_set = f(starting_set)

    if len(new_set) == curr_len:
        return iters
    return fixpoint_rec(new_set, iters + 1)


def main() -> None:
    assert fixpoint({1, 5, 6}) == 1
    assert fixpoint({0, 1}) == 0
    assert fixpoint(set()) == 0
    assert fixpoint({8, 13, 7}) == 2
    assert fixpoint({13, 17, 29}) == 2
    assert fixpoint({13, 47}) == 4


if __name__ == "__main__":
    main()
