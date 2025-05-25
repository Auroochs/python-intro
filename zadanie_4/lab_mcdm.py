import numpy as np
import pandas as pd
from pymcdm.methods import TOPSIS, SPOTIS, VIKOR, PROMETHEE_II
from pymcdm.normalizations import vector_normalization
from pymcdm.weights import entropy_weights

def run_analysis():
    # 1. Dane decyzyjne
    X = np.array([
        [250,  4.5,  12, 500],
        [200,  4.0,  15, 450],
        [300,  4.8,  10, 550],
        [180,  3.9,  20, 400],
        [220,  4.2,  14, 480]
    ], dtype=float)
    alternatives = [f'A{i+1}' for i in range(X.shape[0])]

    # 2. Wagi kryteriów (metoda entropii)
    w = entropy_weights(X, vector_normalization)

    # 3. Typy kryteriów: 1 = maksymalizacja, -1 = minimalizacja
    types = np.array([-1, 1, -1, 1])

    # 4. TOPSIS
    topsis = TOPSIS(normalization_function=vector_normalization)
    topsis_rank = topsis(X, w, types)

    # 5. SPOTIS
    bounds = SPOTIS.make_bounds(X)
    spotis = SPOTIS(bounds)
    spotis_rank = spotis(X, w, types)

    # 6. VIKOR
    vikor = VIKOR(normalization_function=vector_normalization)
    vikor_rank = vikor(X, w, types)

    # 7. PROMETHEE II (funkcja preferencji 'usual')
    prom = PROMETHEE_II('usual')
    prom_rank = prom(X, w, types)

    # 8. Manualna suma ważona (WSM)
    X_vec = vector_normalization(X)
    scores_ws = (X_vec * w).sum(axis=1)
    wsm_rank = scores_ws.argsort()[::-1] + 1

    # 9. Tworzenie DataFrame z wynikami
    df = pd.DataFrame({
        'Alternatywa': alternatives,
        'TOPSIS': topsis_rank,
        'SPOTIS': spotis_rank,
        'VIKOR': vikor_rank,
        'PROMETHEE II': prom_rank,
        'WSM': wsm_rank
    }).set_index('Alternatywa')
    return df

def generate_report(df: pd.DataFrame):
    # Konwersja tabeli wyników na markdown
    table_md = df.to_markdown()
    report_content = f"""# Raport z analizy MCDM

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

{table_md}

## 4. Analiza i wnioski
- **Zbieżność rankingów:**  
- **Różnice:**  
- **Wnioski:**  

## 5. Załączniki
- `lab_mcdm.py` – skrypt wykonujący obliczenia.  
- `wyniki_mcdm.csv` – wygenerowane wyniki.  
- `raport.md` – niniejszy raport.  
"""
    with open('raport.md', 'w', encoding='utf-8') as f:
        f.write(report_content)

def main():
    df = run_analysis()
    print("Wyniki analizy MCDM:")
    print(df, "\n")
    df.to_csv('wyniki_mcdm.csv')
    print("Zapisano wyniki w 'wyniki_mcdm.csv'.")
    generate_report(df)
    print("Raport zapisano w 'raport.md'.")


if __name__ == '__main__':
    main()
