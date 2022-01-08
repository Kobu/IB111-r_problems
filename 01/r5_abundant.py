# † Napište predikát ‹is_abundant›, který je pravdivý, pokud je
# číslo ‹number› abundantní, t.j. je menší, než součet jeho
# vlastních dělitelů (všech dělitelů s výjimkou sebe sama).

from math import sqrt


def is_abundant(number: int) -> bool:
    current_sum = -number

    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            current_sum += i + number // i
            if current_sum > number:
                return True

    return False


def main() -> None:
    assert is_abundant(12)
    assert is_abundant(18)
    assert is_abundant(20)
    assert is_abundant(24)
    assert is_abundant(36)
    assert is_abundant(100)
    assert is_abundant(120)

    assert not is_abundant(7)
    assert not is_abundant(15)
    assert not is_abundant(55)
    assert not is_abundant(62)
    assert not is_abundant(130)


if __name__ == "__main__":
    main()
