# † «Mean filter» je běžný filtr sloužící na odstranění drobných vad
# z obrázku. Funguje tak, že lokálně přílišně se odlišující pixely
# považuje za chybné a napravuje je přiblížením jejich hodnoty
# hodnotám okolních pixelů. To realizuje tak, že každý pixel nahradí
# průměrem jeho původní hodnoty s hodnotami okolních pixelů.

# Napište proceduru, která v parametru dostane obrázek reprezentován
# obdélníkovým dvourozměrným seznamem (délky všech vnitřních seznamů
# jsou stejné) a tento obrázek upraví aplikací mean filtru. Nové
# hodnoty jednotlivých pixelů přesněji spočítá tak, že zaokrouhlí
# průměr hodnot daného pixelu a všech jeho osmi sousedních pixelů,
# přičemž za sousední považujeme všechny pixely, které se ho
# dotýkají stranou nebo rohem. (Pro zaokrouhlování použijte
# vestavěnou funkci ‹round›.)
from typing import List, Optional

Image = List[List[int]]


def get_pixel(x: int, y: int, image: Image) -> Optional[int]:
    height = len(image)
    width = len(image[0])

    if 0 <= x < width and 0 <= y < height:
        return image[y][x]
    return None


def get_neighbours(x: int, y: int, image: Image) -> List[int]:
    result = []
    for i in range(-1, 1 + 1):
        for j in range(-1, 1 + 1):
            pixel = get_pixel(x + i, y + j, image)
            if pixel is not None:
                result.append(pixel)
    return result


def mean_filter(image: Image) -> None:
    new_image = []

    for y, row in enumerate(image):
        new_row = []
        for x, val in enumerate(row):
            res = get_neighbours(x, y, image)
            new_row.append(round(sum(res) / len(res)))
        new_image.append(new_row)

    for y, row in enumerate(new_image):
        for x, val in enumerate(row):
            image[y][x] = val


def main() -> None:
    check_mean_filter([[1]], [[1]])
    check_mean_filter([[1, 1], [1, 1]], [[1, 1], [1, 1]])
    check_mean_filter([[1, 2], [3, 4]], [[2, 2], [2, 2]])
    check_mean_filter([[3, 2, 4]], [[2, 3, 3]])
    check_mean_filter([[1, 1], [3, 3]], [[2, 2], [2, 2]])
    check_mean_filter([[5, 8, 10, 12], [1, 2, 3, 4]], [[4, 5, 6, 7], [4, 5, 6, 7]])
    check_mean_filter(
        [[1, 2, 3], [3, 2, 4], [7, 8, 9], [4, 5, 6]],
        [[2, 2, 3], [4, 4, 5], [5, 5, 6], [6, 6, 7]],
    )


def check_mean_filter(original_image: Image, expected_result: Image) -> None:
    mean_filter(original_image)
    assert original_image == expected_result


if __name__ == "__main__":
    main()
