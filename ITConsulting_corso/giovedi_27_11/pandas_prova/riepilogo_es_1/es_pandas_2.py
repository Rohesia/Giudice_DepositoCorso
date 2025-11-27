import pandas as pd 
import numpy as np 
# ------------------------------
# 1. Caricamento del dataset 
# ------------------------------

df = (pd.read_csv('vendita.csv')
      .drop_duplicates() 
      .dropna(subset=['Quantità', 'Prezzo_Unitario', 'Prodotto', 'Città']))  

# visualizzo le prime 5 righe del file csv 
print(df.head())

# shape del dataset
print(f"\nShape: {df.shape[0]} righe, {df.shape[1]} colonne")

# ------------------------------
# 2. Aggiunta colonna totale vendite
# ------------------------------

df['Totale_Vendite'] = np.where(
    (df['Quantità'] > 0) & (df['Prezzo_Unitario'] > 0),
    df['Quantità'] * df['Prezzo_Unitario'],
    np.nan  
)

# -------------------------------
# 3. Raggruppare per Prodotto e calcolare totale vendite
# -------------------------------

totale_per_prodotto = df.groupby('Prodotto', as_index=False).agg(
    Totale_Vendite=('Totale_Vendite','sum'),
    Quantità_Totale=('Quantità','sum')
).sort_values(by='Totale_Vendite', ascending=False)
print("\nTotale vendite: ", totale_per_prodotto)

# -------------------------------
# 4. Prodotto più venduto in termini di Quantità
# -------------------------------
top_prodotto = totale_per_prodotto.nlargest(1, 'Quantità_Totale') 
print(f"  → {top_prodotto['Prodotto'].iloc[0]}")
print(f"  → Quantità totale: {top_prodotto['Quantità_Totale'].iloc[0]:,.0f} unità")
print(f"  → Ricavo generato: €{top_prodotto['Totale_Vendite'].iloc[0]:,.2f}")

# -------------------------------
# 5. Città con il maggior volume di vendite totali
# -------------------------------
totale_per_citta = df.groupby('Città', as_index=False)['Totale_Vendite'].sum()
top_citta = totale_per_citta.nlargest(1, 'Totale_Vendite')
print(f"\nCittà con il maggior volume di vendite:\n{top_citta}")

# -------------------------------
# 6. Creare DataFrame con vendite superiori a 1000 €
# -------------------------------

df['Categoria_Vendita'] = np.where(
    df['Totale_Vendite'] > 1000, 'Alta', 'Normale'
)


# -------------------------------
# 7. Ordinare il DataFrame originale per Totale Vendite decrescente
# -------------------------------
df_ordinato = df.nlargest(len(df), 'Totale_Vendite')  
print(df_ordinato.head())
print(df_ordinato.head())

# -------------------------------
# 8. Numero di vendite per città
# -------------------------------
vendite_per_citta = df['Città'].value_counts().sort_index()
print("\nNumero di vendite per città: ", vendite_per_citta)

