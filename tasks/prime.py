__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    if number > 1:
        for i in range(2, int(number/2)+1):
            if number % i == 0:
                return False
    else:
        return False
    return True

    """
    Функция должна вернуть True если число является простым, иначе - False
    """
