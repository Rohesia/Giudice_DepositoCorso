# ==========================================
# Analisi di vendite 
# ==========================================

import pandas as pd
import numpy as np

# ------------------------------
# 1. Generazione del dataset
# ------------------------------
np.random.seed(42)  

date_range = pd.date_range(start="2025-11-01", end="2025-11-30", freq='D')
citta = ['Roma', 'Milano', 'Napoli']
prodotti = ['Prodotto A', 'Prodotto B', 'Prodotto C']

# Generazione dati vettorializzata
dati = pd.DataFrame({
    'data': np.repeat(date_range, len(citta) * len(prodotti)),
    'citta': np.tile(np.repeat(citta, len(prodotti)), len(date_range)),
    'prodotto': np.tile(prodotti, len(date_range) * len(citta)),
    'vendite': np.random.randint(50, 500, size=len(date_range) * len(citta) * len(prodotti))
})

# ------------------------------
# 2. Colonna vendite cumulative
# ------------------------------
# Vendite cumulative per prodotto
dati['vendite_cumulative'] = dati.groupby('prodotto')['vendite'].cumsum()

# ------------------------------
# 3. Tabella pivot
# ------------------------------
# Media delle vendite per prodotto in ogni città
tabella_pivot = dati.pivot_table(index='citta', columns='prodotto', values='vendite', aggfunc='mean')
print("\nTabella pivot - vendite medie per prodotto e città:")
print(tabella_pivot.round(2))

# ------------------------------
# 4. Aggregazioni con groupby
# ------------------------------
# Vendite totali per prodotto
v_prod = dati.groupby('prodotto')['vendite'].sum().reset_index()
v_prod.rename(columns={'vendite': 'vendite_totali'}, inplace=True)
print("\nVendite totali per prodotto:", v_prod)

# Vendite totali per città
v_citta = dati.groupby('citta')['vendite'].sum().reset_index()
v_citta.rename(columns={'vendite': 'vendite_totali'}, inplace=True)
print("\nVendite totali per città: ", v_citta)

# Prodotto più venduto per città
top_prod = dati.groupby('citta').apply(lambda x: x.groupby('prodotto')['vendite'].sum().idxmax())
print("\nProdotto più venduto per città: ", top_prod)

# Giorno con maggiori vendite totali
g_top = dati.groupby('data')['vendite'].sum().idxmax()
print("\nGiorno con maggiori vendite totali:", g_top.date())

# ------------------------------
# 5. Insight principali
# ------------------------------
print("\nINSIGHT PRINCIPALI:")
prodotto_migliore = v_prod.loc[v_prod['vendite_totali'].idxmax(), 'prodotto']
print(f"- Il prodotto con maggiori vendite totali è: {prodotto_migliore}")

citta_m = v_citta.loc[v_citta['vendite_totali'].idxmax(), 'citta']
print(f"- La città con maggiori vendite totali è: {citta_m}")


print("- Prodotti più venduti per città:")
for c, p in top_prod.items():
    print(f"  {c}: {p}")


