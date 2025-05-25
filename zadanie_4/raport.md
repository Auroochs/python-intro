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

| Alternatywa |   TOPSIS |   SPOTIS |    VIKOR |   PROMETHEE II |   WSM |
|:------------|---------:|---------:|---------:|---------------:|------:|
| A1          |   0.7146 |   0.3412 | 0.03935  |        0.1885  |     3 |
| A2          |   0.5498 |   0.4360 | 0.28284  |       -0.1885  |     1 |
| A3          |   0.6934 |   0.3115 | 0.18894  |        0.3770  |     5 |
| A4          |   0.3066 |   0.6885 | 1.00000  |       -0.3770  |     2 |
| A5          |   0.6099 |   0.4015 | 0.16061  |        0.0000  |     4 |

## 4. Analiza i wnioski

**Zbieżność rankingów:**  
- Alternatywa **A1** osiąga najlepsze lub drugie wyniki we wszystkich metodach (TOPSIS: 1., VIKOR: 1., PROMETHEE II: 2., SPOTIS: 2., WSM: 3.), co świadczy o jej stabilnej przewadze.  
- Alternatywa **A3** znajduje się wysoko w metodach odległościowych i przewag netto (TOPSIS: 2., SPOTIS: 1., PROMETHEE II: 1.), lecz wypada słabiej w WSM (5.) i VIKOR (3.), co pokazuje wrażliwość na schemat agregacji.

**Różnice:**  
- **WSM** faworyzuje **A2** (1.) dzięki wysokim surowym wartościom kryteriów, podczas gdy **SPOTIS** i **VIKOR** preferują **A1**.  
- **PROMETHEE II** wyróżnia **A3** (1.), podczas gdy w TOPSIS zajmuje ona drugie miejsce.  
- Metody oparte na odległościach (TOPSIS, SPOTIS) i transformacyjne (VIKOR) często wspierają te same alternatywy (przede wszystkim A1), natomiast **WSM** i **PROMETHEE II** ukazują inne preferencje.

**Wnioski:**  
- **Alternatywa A1** jest najbardziej uniwersalnym wyborem — regularnie plasuje się w czołówce we wszystkich metodach.  
- **Alternatywa A3** jest rekomendowana, jeśli kluczowe są metody oparte na przewagach netto i minimalnych odległościach.  
- **Alternatywa A2** może być atrakcyjna w scenariuszu maksymalizacji sumarycznej (WSM), ale słabiej wypada w PROMETHEE II i TOPSIS.  
- Zalecamy wybór **A1** jako najbardziej kompromisową i stabilną opcję.

## 5. Załączniki
- `lab_mcdm.py` – skrypt wykonujący obliczenia.  
- `wyniki_mcdm.csv` – wygenerowane wyniki.  
- `raport.md` – niniejszy raport.
