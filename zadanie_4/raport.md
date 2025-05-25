# Raport z analizy MCDM

## 1. Wstęp
Celem tego laboratorium było przeprowadzenie analizy wielokryterialnej (MCDM) dla zestawu pięciu alternatyw i czterech kryteriów przy użyciu metod: TOPSIS, SPOTIS, VIKOR, PROMETHEE II oraz WSM.

## 2. Przygotowanie danych
- **Alternatywy:** A1, A2, A3, A4, A5  
- **Kryteria:**  
  1. koszt (minimalizacja)  
  2. jakość (maksymalizacja)  
  3. ryzyko (minimalizacja)  
  4. zysk (maksymalizacja)  
- **Wagi:** obliczone metodą entropii.

## 3. Wyniki
Poniższa tabela prezentuje ranking alternatyw:

| Alternatywa   |   TOPSIS |   SPOTIS |     VIKOR |   PROMETHEE II |   WSM |
|:--------------|---------:|---------:|----------:|---------------:|------:|
| A1            | 0.714588 | 0.341185 | 0.0393479 |       0.18848  |     3 |
| A2            | 0.549812 | 0.435992 | 0.282842  |      -0.18848  |     1 |
| A3            | 0.693398 | 0.31152  | 0.188941  |       0.376961 |     5 |
| A4            | 0.306602 | 0.68848  | 1         |      -0.376961 |     2 |
| A5            | 0.609854 | 0.401476 | 0.160607  |       0        |     4 |

## 4. Analiza i wnioski
- **Zbieżność rankingów:**  
- **Różnice:**  
- **Wnioski:**  

## 5. Załączniki
- `lab_mcdm.py` – skrypt wykonujący obliczenia.  
- `wyniki_mcdm.csv` – wygenerowane wyniki.  
- `raport.md` – niniejszy raport.  
