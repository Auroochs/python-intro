# Import modułu math, który zawiera funkcje matematyczne.
# Dokumentacja modułu math: https://docs.python.org/3/library/math.html
import math

# Tworzymy dwie listy, które będziemy łączyć przy użyciu funkcji zip().
list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 20, 30, 40, 50, 60]

# Używamy funkcji zip() do połączenia list.
# Funkcja zip() łączy elementy z iterowalnych obiektów, tworząc krotki,
# w których każdy element pochodzi z odpowiadającego sobie indeksu oryginalnych list.
# Dokumentacja funkcji zip(): https://docs.python.org/3/library/functions.html#zip
zipped_list = list(zip(list1, list2))
print("Połączone listy przy użyciu zip():", zipped_list)

# Przykład użycia funkcji z modułu math:
# Obliczamy pierwiastek kwadratowy z sumy elementów listy list1.
# Funkcja sqrt() oblicza pierwiastek kwadratowy, dokumentacja: https://docs.python.org/3/library/math.html#math.sqrt
try:
    suma_listy = sum(list1)
    wynik = math.sqrt(suma_listy)
    print("Pierwiastek kwadratowy z sumy listy list1 (", suma_listy, "):", wynik)
except ValueError as e:
    # Obsługa wyjątku ValueError, który może zostać zgłoszony, gdy funkcja math.sqrt otrzyma nieodpowiednią wartość.
    # Dokumentacja wyjątku ValueError: https://docs.python.org/3/library/exceptions.html#ValueError
    print("Wystąpił ValueError:", e)
