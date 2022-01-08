# Napište funkci, která zploští seznam seznamů do jednoho nového
# seznamu tak, že vnořené seznamy pospojuje za sebe.
from typing import List, Union, Callable


# Credits: XLAQO#1432


def concat1(lists: List[List[int]]) -> List[int]:
    res = []

    for lst in lists:
        for el in lst:
            res.append(el)
    return res


def concat2(lists: List[List[int]]) -> List[int]:
    return [el for lst in lists for el in lst]


NestedListItem = Union[int, "NestedList"]


class NestedList:
    def __init__(self, a_list: List[NestedListItem]):
        self.list = a_list


def concat3(lists: NestedList) -> List[int]:
    res = []

    for el in lists.list:
        if isinstance(el, int):
            res.append(el)
        else:
            res.extend(concat3(el))
    return res


def test_original(fun: Callable[[List[List[int]]], List[int]]) -> None:
    assert fun([[1], [2], [1, 2]]) == [1, 2, 1, 2]
    assert fun([[0, 40, 1], [43, -1], [2]]) == [0, 40, 1, 43, -1, 2]
    assert fun([[1]]) == [1]
    assert fun([[], [1], []]) == [1]
    assert fun([[1, 1, 1], [1], [1, 1]]) == [1, 1, 1, 1, 1, 1]


def test_nested(fun: Callable[[NestedList], List[int]]) -> None:
    assert fun(NestedList([])) == []
    assert fun(NestedList([1, 2, 3])) == [1, 2, 3]
    assert fun(
        NestedList([NestedList([NestedList([NestedList([1])]), NestedList([2])]), 3])
    ) == [1, 2, 3]
    assert fun(
        NestedList(
            [NestedList([1, 2]), NestedList([NestedList([7, 4]), NestedList([5])])]
        )
    ) == [1, 2, 7, 4, 5]


def main() -> None:
    test_original(concat1)
    test_original(concat2)
    test_nested(concat3)


if __name__ == "__main__":
    main()
