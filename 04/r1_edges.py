# Jednou ze základních metod digitálního zpracování obrazu je
# detekce hran. V tomto kontextu hranou chápeme oblast s ostrým
# kontrastem: nemusí jít nutně o hranice mezi objekty, ale třeba
# také změny textury, rozhraní mezi světlem a tmou, atd. Hrany se
# v obrázcích detekují na základě velké změny jasu sousedních pixelů
# (více o informací naleznete například ve Wikipedii pod heslem
# „Edge detection“).

# V této úloze si vyzkoušíte zjednodušený způsob, jak nalézt všechny
# hrany v daném obrázku, a vytvořit nový obrázek, který obsahuje
# pouze nalezené hrany.

# Napište (čistou) funkci, která na vstupu dostane obrázek
# reprezentovaný obdélníkovým seznamem seznamů (délky všech
# vnitřních seznamů jsou stejné) celých čísel a vrátí nový obrázek
# stejné velikosti, který obsahuje pouze hrany původního obrázku.
# Konkrétně pixely ve výsledném obrázku, kde na vstupu detekujeme
# hranu, budou mít hodnotu 1 a všechny ostatní hodnotu 0.

# Funkce bude brát krom vstupního obrázku ještě číselný parametr,
# který určí, o kolik se dva pixely musí nejméně lišit, abychom je
# označili za hranu. Konkrétně pak za součást nějaké hrany
# považujeme každý pixel, který se liší od některého ze svých čtyř
# sousedů alespoň o tuto hodnotu.
from typing import List

Image = List[List[int]]


def is_edge(cell1: int, cell2: int, threshold: int) -> int:
    return int(abs(cell1 - cell2) >= threshold)


# 0 [0, 2, 1, 1, 0]
# 1 [3, 0, 1, 1, 1]
# 2 [0, 0, 1, 1, 0]
# 3 [0, 7, 1, 1, 0]
# 4 [0, 0, 1, 1, 4]
#    0  1  2  3  4


def find_edges(image: Image, threshold: int) -> Image:
    height = len(image)
    width = len(image[0])

    new_image = []
    for y, row in enumerate(image):
        new_row = []
        for x, val in enumerate(row):
            new_cell = 0
            # if can look right
            if x != width - 1:
                new_cell = max(new_cell, is_edge(val, image[y][x + 1], threshold))
            # if can look left
            if x != 0:
                new_cell = max(new_cell, is_edge(val, image[y][x - 1], threshold))
            # if can look up
            if y != 0:
                new_cell = max(new_cell, is_edge(val, image[y - 1][x], threshold))
            # if can look down
            if y != height - 1:
                new_cell = max(new_cell, is_edge(val, image[y + 1][x], threshold))

            new_row.append(new_cell)
        new_image.append(new_row)

    return new_image


def main() -> None:
    assert find_edges([[1, 1], [1, 1]], 2) == [[0, 0], [0, 0]]
    assert find_edges([[1, 1, 1, 3, 3], [1, 1, 3, 3, 3], [1, 1, 1, 3, 3]], 2) == [
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 1, 1, 0],
    ]
    assert find_edges([[1, 1, 1, 3, 3], [1, 1, 3, 3, 3], [1, 1, 1, 3, 3]], 3) == [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert find_edges(
        [
            [
                1,
                1,
                1,
                2,
                2,
                2,
                1,
                2,
            ],
            [2, 1, 1, 1, 10, 2, 1, 2],
            [1, 1, 1, 9, 10, 10, 1, 2],
            [1, 2, 1, 2, 9, 2, 1, 2],
            [2, 1, 1, 1, 1, 2, 1, 2],
            [2, 2, 2, 1, 1, 2, 1, 2],
        ],
        6,
    ) == [
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
    assert find_edges(
        [
            [
                1,
                1,
                1,
                2,
                2,
                2,
                1,
                2,
            ],
            [2, 1, 1, 1, 10, 2, 1, 2],
            [1, 1, 1, 9, 10, 10, 1, 2],
            [1, 2, 1, 2, 9, 2, 1, 2],
            [2, 1, 1, 1, 1, 2, 1, 2],
            [2, 2, 2, 1, 1, 2, 1, 2],
        ],
        8,
    ) == [
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]


if __name__ == "__main__":
    main()
