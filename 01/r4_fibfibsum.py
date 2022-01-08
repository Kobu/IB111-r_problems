# † Nechť ⟦A⟧ je Fibonacciho posloupnost s členy ⟦aₙ⟧ a ⟦B⟧ je
# posloupnost taková, že má na ⟦i⟧-té pozici ⟦aᵢ⟧-tý prvek
# posloupnosti ⟦A⟧, tj. prvek s indexem ⟦aᵢ⟧ (nikoliv prvek
# s indexem ⟦i⟧). Napište funkci, která sečte prvních ‹count› prvků
# posloupnosti ⟦B⟧ (t.j. ty prvky posloupnosti ⟦A⟧, kterých «indexy»
# jsou po sobě jdoucí Fibonacciho čísla).

# Například ‹fibfibsum(6)› se vypočte takto:
# ⟦ a₁ + a₁ + a₂ + a₃ + a₅ + a₈ = 1 + 1 + 1 + 2 + 5 + 21 = 31 ⟧

# fib 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
#
# A [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# B [1, 1, 1, 2, 5, 21, ...]


# Credits  bobtheskrob#8192


def fib(n: int) -> int:
    a = b = 1
    for i in range(n - 2):
        c = a + b
        a = b
        b = c
    return b


def fibfibsum(count: int) -> int:
    result = 0
    for B in range(1, count + 1):
        result += fib(fib(B))
    return result


def main() -> None:
    assert fibfibsum(3) == 3
    assert fibfibsum(5) == 10
    assert fibfibsum(6) == 31
    assert fibfibsum(7) == 264
    assert fibfibsum(10) == 139589576542


if __name__ == "__main__":
    main()
