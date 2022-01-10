from typing import Dict, Tuple, Callable

# Uvažujme jednoduché aritmetické výrazy se sčítáním a násobením.
# Budeme je ukládat do dvojice slovníků (‹expr› a ‹const›), a to
# následovně:
#
#  • klíč je vždy jméno proměnné (řetězec)
#  • hodnota ve slovníku ‹expr› je trojice:
#    ◦ první složka je operátor ‹'*'› nebo ‹'+'›
#    ◦ druhá a třetí složka jsou operandy – názvy proměnných
#  • hodnota ve slovníku ‹const› je číslo
#
# Každá proměnná se objeví v nejvýše jednom slovníku. Proměnné,
# které se nenachází v žádném z nich jsou rovny nule.

# Napište čistou funkci, která dostane jako parametry slovníky
# ‹expr› a ‹const› a název proměnné. Výsledkem bude hodnota této
# proměnné. Při vyhodnocování se Vám bude hodit zásobník a pomocný
# slovník.


OPS: Dict[str, Callable[[int, int], int]] = {
    "*": lambda x, y: x * y,
    "+": lambda x, y: x + y,
}


def evaluate(
    expr: Dict[str, Tuple[str, str, str]], const: Dict[str, int], var: str
) -> int:
    if var in const:
        return const[var]

    if var in expr:
        op, arg1, arg2 = expr[var]

        op_eval = OPS[op]
        arg1_eval = evaluate(expr, const, arg1)
        arg2_eval = evaluate(expr, const, arg2)

        return op_eval(arg1_eval, arg2_eval)

    return 0


def main() -> None:
    assert evaluate({}, {"a": 1}, "a") == 1
    assert evaluate({"x": ("+", "a", "a")}, {"a": 1}, "x") == 2
    assert evaluate({"x": ("+", "a", "b")}, {"a": 1, "b": 2}, "x") == 3
    assert (
        evaluate({"x": ("+", "a", "b"), "y": ("*", "x", "x")}, {"a": 1, "b": 2}, "x")
        == 3
    )
    assert (
        evaluate({"x": ("+", "a", "b"), "y": ("*", "x", "x")}, {"a": 1, "b": 2}, "y")
        == 9
    )


if __name__ == "__main__":
    main()
