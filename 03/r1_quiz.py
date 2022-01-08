# Naprogramujte funkci ‹mark_points›, která spočítá počet bodů,
# které student získal v multiple-choice testu. Vypracované řešení
# je reprezentováno parametrem ‹solution›, kterého prvky odpovídají
# možnostem, které student označil (tzn. je-li ‹solution[0]› rovno
# ‹2›, odpověď na první otázku byla ‹2›). Správné odpovědi jsou
# v parametru ‹answers› jako seznam dvojic, kde pozice v seznamu
# odpovídá číslu otázky, a dvojice je ve formě (správná odpověď,
# body).
from typing import Tuple, List

Question = Tuple[int, int]


def mark_points(answers: List[Question], solution: List[int]) -> int:
    points = 0

    for (cor_answer, points_given), my_answer in zip(answers, solution):
        if cor_answer == my_answer:
            points += points_given

    return points


def main() -> None:
    assert mark_points([(0, 2), (0, 3), (0, 4)], [0, 2, 0]) == 6
    assert mark_points([], []) == 0
    assert mark_points([(1, 1), (2, 1), (0, 1), (2, 1), (4, 1)], [1, 2, 3, 4, 4]) == 3
    assert mark_points([(0, 0), (1, 0), (2, 0)], [4, 3, 1]) == 0
    assert mark_points([(1, 1), (0, 3), (2, 3), (4, 3)], [1, 0, 2, 4]) == 10


if __name__ == "__main__":
    main()
