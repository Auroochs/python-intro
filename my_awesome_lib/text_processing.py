"""
Moduł: text_processing
Funkcje do przetwarzania tekstu, takie jak liczenie słów, odwracanie ciągów znaków czy sprawdzanie palindromów.
"""


def count_words(text):
    """
    Zlicza liczbę słów w podanym tekście.

    :param text: Tekst do analizy.
    :return: Liczba słów.
    """
    return len(text.split())


def reverse_text(text):
    """
    Odwraca podany tekst.

    :param text: Tekst do odwrócenia.
    :return: Odwrócony tekst.
    """
    return text[::-1]


def is_palindrome(text):
    """
    Sprawdza, czy podany tekst jest palindromem (ignoruje spacje i wielkość liter).

    :param text: Tekst do sprawdzenia.
    :return: True, jeśli tekst jest palindromem, w przeciwnym razie False.
    """
    cleaned = ''.join(text.split()).lower()
    return cleaned == cleaned[::-1]
