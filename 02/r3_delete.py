# Napište funkci ‹delete_to_maximal›, která pro dané číslo ‹number›
# najde největší možné číslo, které lze získat smazáním jedné
# desítkové cifry.
from typing import List, Callable


# Credits: bobtheskrob#8192


def delete_to_maximal(number: int) -> int:
    counter = number
    dig_exp = 1
    result = 0
    while counter > 0:
        number_ = (number // 10 ** dig_exp) * 10 ** (dig_exp - 1) + number % 10 ** (
            dig_exp - 1
        )
        if number_ > result:
            result = number_
        dig_exp += 1
        counter //= 10
    return result


def delete_k_to_maximal(number: int, k: int) -> int:
    for _ in range(k):
        number = delete_to_maximal(number)
    return number


# --------------------------------------------
def num_to_list(num: int) -> List[int]:
    res = []

    while num:
        res.append(num % 10)
        num //= 10

    res.reverse()
    return res


def list_to_num(nums: List[int]) -> int:
    res = 0

    for num in nums:
        res *= 10
        res += num

    return res


def test_conversion() -> None:
    for i in range(1000000 + 1):
        assert list_to_num(num_to_list(i)) == i
    print("PASSED")


def delete_to_maximal2(number: int) -> int:
    in_list = num_to_list(number)

    for i in range(1, len(in_list)):
        if in_list[i - 1] < in_list[i]:
            return list_to_num(in_list[: i - 1] + in_list[i:])
    return list_to_num(in_list[:-1])


# Napište funkci ‹delete_k_to_maximal›, která pro dané číslo
# ‹number› najde největší možné číslo, které lze získat smazáním
# (vynecháním) ‹k› desítkových cifer.


def delete_k_to_maximal2(number: int, k: int) -> int:
    for i in range(k):
        number = delete_to_maximal2(number)

    return number


def main(fun1: Callable[[int], int], fun2: Callable[[int, int], int]) -> None:
    # test_conversion()
    assert fun1(54) == 5
    assert fun1(45) == 5
    assert fun1(100) == 10
    assert fun1(123) == 23
    assert fun1(4312) == 432
    assert fun1(1231) == 231
    assert fun1(2331) == 331

    assert fun2(2331, 2) == 33
    assert fun2(22331, 2) == 331
    assert fun2(12345, 4) == 5
    assert fun2(1234554321, 8) == 55
    assert fun2(123123123123, 4) == 33123123
    assert fun2(123321123321, 4) == 33223321
    assert fun2(11181118111, 9) == 88


if __name__ == "__main__":
    main(delete_to_maximal, delete_k_to_maximal)
    main(delete_to_maximal2, delete_k_to_maximal2)
