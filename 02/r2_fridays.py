# Napište funkci, která spočítá počet pátků 13. v daném roce ‹year›.
# Parametr ‹day_of_week› udává den v týdnu, na který v daném roce
# padne 1. leden. Dny v týdnu mají hodnoty 0–6, počínaje pondělím
# s hodnotou 0.


# Credits: tomsko#4828

TARGET = 13


def check_leap(year: int) -> bool:
    return (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)


def fridays_in_month(first_day: int) -> bool:
    return (first_day + TARGET - 1) % 7 == 4


def fridays(year: int, day_of_week: int) -> int:
    counter = 0
    months = [31, 28 + int(check_leap(year)), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for month in months:
        if fridays_in_month(day_of_week):
            counter += 1
        day_of_week += month
        day_of_week = day_of_week % 7
    return counter


def main() -> None:
    assert fridays(2020, 2) == 2
    assert fridays(2019, 1) == 2
    assert fridays(2018, 0) == 2
    assert fridays(2017, 6) == 2
    assert fridays(2016, 4) == 1
    assert fridays(2015, 3) == 3
    assert fridays(2012, 6) == 3
    assert fridays(2000, 5) == 1
    assert fridays(1996, 0) == 2
    assert fridays(1643, 3) == 3
    assert fridays(1501, 1) == 2


if __name__ == "__main__":
    main()
