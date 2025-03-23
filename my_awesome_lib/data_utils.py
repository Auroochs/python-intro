"""
Moduł: data_utils
Funkcje pomocnicze do operacji na danych, np. odczyt i zapis plików CSV oraz transformacja danych.
"""

import csv


def read_csv(file_path):
    """
    Odczytuje plik CSV i zwraca listę wierszy.

    :param file_path: Ścieżka do pliku CSV.
    :return: Lista wierszy z pliku CSV.
    """
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        return list(reader)


def write_csv(file_path, data):
    """
    Zapisuje dane do pliku CSV.

    :param file_path: Ścieżka do pliku CSV.
    :param data: Lista wierszy do zapisania.
    """
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def transform_data(data, transform_func):
    """
    Przekształca dane przy użyciu podanej funkcji transformującej.

    :param data: Lista danych.
    :param transform_func: Funkcja przekształcająca pojedynczy element.
    :return: Lista przekształconych danych.
    """
    return [transform_func(item) for item in data]
