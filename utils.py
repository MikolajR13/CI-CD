"""
utils.py - Moduł zawierający funkcje pomocnicze do podstawowych operacji matematycznych.
"""


def add(a: int, b: int) -> int:
    """
    Dodaje dwie liczby całkowite.

    Parameters:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.

    Returns:
        int: Wynik dodawania a i b.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Odejmuje jedną liczbę od drugiej.

    Parameters:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.

    Returns:
        int: Wynik odejmowania b od a.
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Mnoży dwie liczby całkowite.

    Parameters:
        a (int): Pierwsza liczba.
        b (int): Druga liczba.

    Returns:
        int: Wynik mnożenia a i b.
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Dzieli jedną liczbę przez drugą.

    Parameters:
        a (int): Liczba dzielona.
        b (int): Liczba przez którą dzielimy.

    Returns:
        float: Wynik dzielenia a przez b (zawsze zwraca float).
    """
    return a / b
