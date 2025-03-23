"""
Moduł: math_tools
Zbiór podstawowych operacji matematycznych.
"""


def add(a, b):
    """
    Zwraca sumę dwóch liczb.

    :param a: Pierwsza liczba.
    :param b: Druga liczba.
    :return: Suma a + b.
    """
    return a + b


def subtract(a, b):
    """
    Zwraca różnicę dwóch liczb.

    :param a: Pierwsza liczba.
    :param b: Druga liczba.
    :return: Wynik a - b.
    """
    return a - b


def multiply(a, b):
    """
    Zwraca iloczyn dwóch liczb.

    :param a: Pierwsza liczba.
    :param b: Druga liczba.
    :return: Iloczyn a * b.
    """
    return a * b


def divide(a, b):
    """
    Zwraca wynik dzielenia dwóch liczb.

    :param a: Licznik.
    :param b: Mianownik.
    :return: Wynik a / b.
    :raises ValueError: Jeśli b jest zerem.
    """
    if b == 0:
        raise ValueError("Dzielenie przez zero nie jest dozwolone.")
    return a / b
