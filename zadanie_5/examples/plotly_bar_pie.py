import pandas as pd
import plotly.express as px

# Przygotowanie danych
df = pd.DataFrame({
    'Owoc': ['Jabłka', 'Pomarancze', 'Banany', 'Kiwi'],
    'Liczba': [10, 15, 7, 3]
})

# --- 1) Wykres słupkowy ---
fig = px.bar(df, x='Owoc', y='Liczba', title='Ilość owoców')
fig.write_html('bar_chart.html')
fig.show()

# --- 2) Wykres kołowy ---
fig2 = px.pie(df, values='Liczba', names='Owoc', title='Udział owoców')
fig2.write_html('pie_chart.html')
fig2.show()
