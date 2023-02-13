from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    minlen = min(len(arr1), len(arr2))
    result = [(i,j) for i in arr1[:minlen] for j in arr2[:minlen]]
    jump = minlen + 1
    return result[::jump]

    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """

