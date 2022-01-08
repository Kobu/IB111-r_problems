# † Napište čistou funkci, která k zadanému číslu najde nejbližší
# takové, že se tyto od sebe liší na každé pozici svého desítkového
# zápisu. Nalezené a vstupní číslo nemusí mít stejný počet cifer.
#
# Příklad: 123 a 222 se liší v první a třetí pozici, na druhé jsou
# ale shodné. Čísla 1234 a 4321 se liší na všech pozicích.


def are_distinct(x: int, y: int) -> bool:
    y = abs(y)
    x = abs(x)

    while x and y:
        if x % 10 == y % 10:
            return False

        x //= 10
        y //= 10
    return True


def distinct(num: int) -> int:
    distance = 1

    while True:
        if are_distinct(num, num - distance):
            return num - distance
        elif are_distinct(num, num + distance):
            return num + distance
        else:
            distance += 1


def main() -> None:
    assert abs(distinct(2) - 2) == 1
    assert abs(distinct(-7) + 7) == 1
    assert abs(distinct(0)) == 1

    assert distinct(253) == 300
    assert distinct(7802) == 8010
    assert distinct(-25) == -30

    assert distinct(999) == 1000
    assert distinct(-95) == -100
    assert distinct(90) == 89

    assert distinct(1234) == 999
    assert distinct(1543) == 2000
    assert distinct(-100) == -99


if __name__ == "__main__":
    main()
