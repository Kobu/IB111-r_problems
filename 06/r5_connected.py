from typing import Dict, List, Set

# † Uvažme městskou hromadnou dopravu, která má pojmenované zastávky,
# mezi kterými jezdí (pro nás anonymní) spoje. Spoje mají daný směr:
# není zaručeno, že jede-li spoj z ⟦A⟧ do ⟦B⟧, jede i spoj z ⟦B⟧ do
# ⟦A⟧. Dopravní síť budeme reprezentovat slovníkem, kde klíčem je
# nějaká zastávka ⟦A⟧, a jemu příslušnou hodnotou je seznam
# zastávek, do kterých se lze z ⟦A⟧ dopravit bez dalšího zastavení.

# Napište predikát, který rozhodne, je-li možné dostat se
# z libovolné zastávky na libovolnou jinou zastávku pouze použitím
# spojů ze zadaného slovníku.

Stops = Dict[str, List[str]]


# iterative
def all_connected(stops: Stops) -> bool:
    return all(is_reachable_out(start, stops) for start in stops)


def is_reachable_out(start: str, stops: Stops) -> bool:
    old_len = 0
    reachable = {start}

    while len(reachable) != old_len:
        old_len = len(reachable)
        new_reachable = reachable.copy()

        for stop in reachable:
            new_reachable.update(set(stops[stop]))

        reachable = new_reachable

    return all(el in reachable for el in stops.keys())


# --------------------------------------------------------------------


# backtracking=ish
def all_connected2(stops: Stops) -> bool:
    if len(stops) == 1:
        return True

    for start in stops:
        for target in stops:
            if not connected_check(start, target, stops, set()):
                return False
    return True


def connected_check(start: str, target: str, stops: Stops, visited: Set[str]) -> bool:
    if start in visited:
        return False

    visited.add(start)
    reachable = stops[start]

    if target in reachable:
        return True

    for stop in reachable:
        can_reach = connected_check(stop, target, stops, visited)
        if can_reach:
            return True
    return False


def main() -> None:
    assert all_connected({"A": []})
    assert all_connected({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]})
    assert all_connected({"A": ["B"], "B": ["C"], "C": ["D"], "D": ["A"]})
    assert all_connected(
        {"A": ["B", "C", "D"], "B": ["C"], "C": ["A", "B"], "D": ["C"]}
    )

    assert not all_connected({"A": ["B"], "B": []})
    assert not all_connected({"A": ["B", "C"], "B": ["C"], "C": ["B"]})
    assert not all_connected({"A": ["B", "C"], "B": ["C"], "C": ["B"]})
    assert not all_connected({"A": ["B", "C", "D"], "B": ["C"], "C": ["B"], "D": ["A"]})


if __name__ == "__main__":
    main()
