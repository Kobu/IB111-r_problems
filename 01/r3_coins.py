# Uvažme, že chceme přesně zaplatit sumu ‹value› českými mincemi
# (denominace 1, 2, 5, 10, 20 a 50 korun). Spočtěte, kolik nejméně
# mincí potřebujeme.
from typing import Callable


def coins2(value: int) -> int:
    coins_inc = [1, 2, 5, 10, 20, 50]
    count = 0
    current_coin = coins_inc.pop()

    while value != 0:
        if value >= current_coin:
            value -= current_coin
            count += 1
        else:
            current_coin = coins_inc.pop()
    return count


COINS_DEC = [50, 20, 10, 5, 2, 1]


def coins(value: int) -> int:
    count = 0

    for coin in COINS_DEC:
        amount = value // coin
        value -= amount * coin
        count += amount
    return count


def main(fun: Callable[[int], int]) -> None:
    assert fun(10) == 1
    assert fun(23) == 3
    assert fun(48) == 5
    assert fun(92) == 4
    assert fun(314) == 9
    assert fun(1043) == 24


if __name__ == "__main__":
    main(coins)
    main(coins2)
