__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    even, odd = 0, 0
    for i in arr:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    if odd:
        return even/odd
    else:
        return 0

    # """
    # Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    # Пример:
    # even_odd([1, 2, 3, 4, 5]) == 0.8889
    # """
