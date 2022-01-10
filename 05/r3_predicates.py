from math import sqrt


# Tento příklad bude mírně nekonvenční v tom, že nebudete
# programovat nové funkce. Vaším úkolem bude naopak poznat, co
# zadaná funkce počítá a napsat testy, které Vaši hypotézu ověří.
# Každá funkce zde zadaná je predikát a většina má nějakou vstupní
# podmínku. Samotné funkce i proměnné v nich jsou záměrně
# pojmenované tak, aby Vám názvy nic neřekly.

# ci y je x-ty prvok fibonnaciho postupnosti
def f_1(x: int, y: int) -> bool:
    assert y >= 1
    assert x >= 1
    a = 0
    b = 1
    while x > 1:
        a, b = b, a + b
        x -= 1
    return b == y


# 1 1 2 3 5 8 13 21 34
def test_f_1() -> None:
    assert f_1(1, 1)
    assert f_1(2, 1)
    assert f_1(3, 2)
    assert f_1(6, 8)
    assert f_1(9, 34)
    assert not f_1(9, 21)


# pocet prvocisiel na interval 1 az x // 2 == y + 1
def f_2(x: int, y: int) -> bool:
    assert x > 0
    b = 1
    a = x // 2
    while a >= b:
        if x % b == 0:
            y -= 1
        b += 1
    return y <= 1


# 1 2 3 5 7 11 13 17 19
def test_f_2() -> None:
    assert f_2(2, 1)
    assert f_2(6, 3)
    assert f_2(10, 4)
    assert f_2(40, 8)


# a .. max(x, y)
def f_3(x: int, y: int) -> bool:
    assert x > 0 and y > 0
    a = 1
    b = 0
    while a <= max(x, y):
        if x % a == 0:
            b += 1
        if y % a == 0:
            b -= 1
        a += 1
    return b > 0


def test_f_3() -> None:
    assert f_3(10, 1)
    assert f_3(5, 1)
    assert f_3(32, 16)
    assert f_3(2, 1)
    assert not f_3(100, 200)


# 1 .. x-1, y prvocisiel
def f_4(x: int, y: int) -> bool:
    for z in range(1, x):
        b = True
        for i in range(2, int(sqrt(z)) + 1):
            if z % i == 0:
                b = False
        if b:
            y -= 1
    return y == 0


def test_f_4() -> None:
    assert f_4(1, 0)
    assert f_4(2, 1)
    assert f_4(21, 9)
    assert f_4(11, 5)


def f_5(x: int) -> bool:
    assert x >= 0
    y = 0
    z = x
    while z > 0:
        y = y * 7 + z % 7
        z = z // 7
    return x == y


def test_f_5() -> None:
    assert f_5(400)
    assert f_5(456)
    assert f_5(3249)


def f_6(x: int, y: int) -> bool:
    assert x >= 0
    z = 0
    while x > 0:
        z = z * 2 + (x % 2)
        x = x // 2
    return y == z


def test_f_6() -> None:
    pass


def f_7(x: int, y: int) -> bool:
    assert x >= 0
    z = 2
    while x > 1:
        if x % z == 0:
            y -= 1
        while x % z == 0:
            x = x // z
        z += 1
    return y == 0


def test_f_7() -> None:
    pass


def f_8(x: int, y: int, z: int) -> bool:
    assert x > 0 and y > 0
    d = 2
    r = 0
    while x > 1 and y > 1:
        if x % d == 0 and y % d == 0:
            x = x // d
            y = y // d
            r += 1
        while x % d == 0:
            x = x // d
        while y % d == 0:
            y = y // d
        d += 1
    return r == z


def test_f_8() -> None:
    pass


def main() -> None:
    test_f_1()
    test_f_2()
    test_f_3()
    test_f_4()
    test_f_5()
    test_f_6()
    test_f_7()
    test_f_8()


if __name__ == "__main__":
    main()
