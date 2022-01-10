# Napište predikát ‹is_anagram›, který dostane na vstup 2 řetězce,
# ‹text› a ‹anagram›, složené z velkých písmen anglické abecedy a
# mezer. Predikát nechť rozhodne, zda je řetězec ‹anagram› permutací
# řetězce ‹text› (mezery přitom ignorujte).

from collections import Counter, defaultdict
from typing import DefaultDict


def is_anagram2(text: str, anagram: str) -> bool:
    parsed1 = text.replace(" ", "")
    parsed2 = anagram.replace(" ", "")

    return sorted(parsed1) == sorted(parsed2)


def is_anagram3(text: str, anagram: str) -> bool:
    parsed1 = text.replace(" ", "")
    parsed2 = anagram.replace(" ", "")

    return Counter(parsed1) == Counter(parsed2)


def is_anagram(text: str, anagram: str) -> bool:
    parsed1 = text.replace(" ", "")
    parsed2 = anagram.replace(" ", "")

    counter1: DefaultDict[str, int] = defaultdict(int)
    counter2: DefaultDict[str, int] = defaultdict(int)

    for char in parsed1:
        counter1[char] += 1
    for char in parsed2:
        counter2[char] += 1

    return counter1 == counter2


def main() -> None:
    assert is_anagram("ABC", "ACB")
    assert is_anagram(" ABC", "ACB ")
    assert is_anagram(" A  BC", "ACB ")
    assert is_anagram("B BB C", "CBBB")
    assert is_anagram("     ", "")

    assert not is_anagram("ABC", "EFG")
    assert not is_anagram("ABCC", "ACB")
    assert not is_anagram(" A    ", " ")
    assert not is_anagram("B BB ", "B")
    assert not is_anagram("B BB ", "BC")


if __name__ == "__main__":
    main()
