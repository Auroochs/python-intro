# Lab 5 – Wizualizacja danych

Krótki opis projektu i celu laboratorium.

## Spis treści

- [Opis](#opis)  
- [Wymagania](#wymagania)  
- [Instalacja](#instalacja)  
- [Struktura projektu](#struktura-projektu)  
- [Uruchomienie przykładów](#uruchomienie-przykładów)  
- [Raport](#raport)  
- [Linki](#linki)  
- [Licencja](#licencja)  

---

## Opis

Projekt demonstruje podstawowe techniki wizualizacji danych w Pythonie z wykorzystaniem bibliotek Matplotlib oraz Plotly. Zawiera przykładowe skrypty generujące wykresy liniowe, punktowe, słupkowe i kołowe.

## Wymagania

- Python ≥ 3.7  
- biblioteki: `numpy`, `pandas`, `matplotlib`, `plotly`

## Instalacja

1. Sklonuj repozytorium:  
   ```bash
   git clone https://github.com/TwojNick/lab5-wizualizacja.git
   cd lab5-wizualizacja
   ```
2. Utwórz i aktywuj środowisko wirtualne:  
   ```bash
   python3 -m venv env
   source env/bin/activate    # Linux/macOS
   .\env\Scripts\activate  # Windows
   ```
3. Zainstaluj zależności:  
   ```bash
   pip install -r requirements.txt
   ```

## Struktura projektu

```
lab5-wizualizacja/
├── examples/
│   ├── matplotlib_line_scatter.py   # wykres liniowy i scatter
│   └── plotly_bar_pie.py            # wykres słupkowy i pie
├── line_plot.png                    # wygenerowany wykres linii
├── scatter_plot.png                 # wygenerowany scatter
├── bar_chart.html                   # wykres słupkowy (Plotly)
├── pie_chart.html                   # wykres kołowy (Plotly)
├── raport.md                        # raport z laboratorium
├── README.md                        # ten plik
└── requirements.txt                 # lista zależności
```

## Uruchomienie przykładów

- **Matplotlib**  
  ```bash
  python examples/matplotlib_line_scatter.py
  ```
  Spowoduje wygenerowanie plików `line_plot.png` i `scatter_plot.png` oraz wyświetlenie wykresów.

- **Plotly**  
  ```bash
  python examples/plotly_bar_pie.py
  ```
  Wygeneruje interaktywne wykresy w plikach `bar_chart.html` i `pie_chart.html`, które możesz otworzyć w przeglądarce.

## Raport

Pełny opis eksperymentów i omówienie bibliotek znajduje się w pliku [`raport.md`](raport.md).

## Linki

- [Dokumentacja Matplotlib](https://matplotlib.org/)  
- [Dokumentacja Plotly](https://plotly.com/python/)

## Licencja

Ten projekt jest udostępniony na licencji MIT.
