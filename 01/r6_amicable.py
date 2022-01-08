# † Napište predikát, který určí, jsou-li 2 čísla spřátelená
# (amicable). Spřátelená čísla jsou dvě přirozená čísla taková, že
# součet všech kladných dělitelů jednoho čísla (kromě čísla
# samotného) se rovná druhému číslu, a naopak – součet všech
# dělitelů druhého čísla (kromě něho samotného) se rovná prvnímu.

from math import sqrt


def sum_divisors(num: int) -> int:
    if num == 1:
        return 0

    current_sum = -num
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            current_sum += i + num // i

    return current_sum


def amicable(a: int, b: int) -> bool:
    return a == sum_divisors(b) and b == sum_divisors(a)


def main() -> None:
    assert not amicable(136, 241)
    assert not amicable(1, 1)
    assert amicable(220, 284)
    assert amicable(1184, 1210)
    assert amicable(2620, 2924)
    assert not amicable(1190, 1212)
    assert not amicable(349, 234)


if __name__ == "__main__":
    main()
