import pandas as pd 

# ------------------------------
# 1. Caricamento del dataset 
# ------------------------------

df = pd.read_csv('vendita.csv')

# visualizzo le prime 5 righe del file csv 
print(df.head())

# ------------------------------
# 2. Aggiunta colonna totale vendite
# ------------------------------

df = df.assign(Totale_Vendite = df['Quantità'] * df['Prezzo_Unitario'])
print(df.head())




# -------------------------------
# 3. Raggruppare per Prodotto e calcolare totale vendite
# -------------------------------

totale_per_prodotto = df.groupby('Prodotto', as_index=False).agg(
    Totale_Vendite=('Totale_Vendite','sum'),
    Quantità_Totale=('Quantità','sum')
).sort_values(by='Totale_Vendite', ascending=False)
print("\nTotale vendite e quantità per prodotto:")
print(totale_per_prodotto)

# -------------------------------
# 4. Prodotto più venduto in termini di Quantità
# -------------------------------
top_prodotto = totale_per_prodotto.nlargest(1, 'Quantità_Totale')
print(f"\nProdotto più venduto in quantità:\n{top_prodotto[['Prodotto','Quantità_Totale']]}")

# -------------------------------
# 5. Città con il maggior volume di vendite totali
# -------------------------------
totale_per_citta = df.groupby('Città', as_index=False)['Totale_Vendite'].sum()
top_citta = totale_per_citta.nlargest(1, 'Totale_Vendite')
print(f"\nCittà con il maggior volume di vendite:\n{top_citta}")

# -------------------------------
# 6. Creare DataFrame con vendite superiori a 1000 €
# -------------------------------
vendite_alte = df.query('Totale_Vendite > 1000')
print(vendite_alte.head())

# -------------------------------
# 7. Ordinare il DataFrame originale per Totale Vendite decrescente
# -------------------------------
df_ordinato = df.nlargest(len(df), 'Totale_Vendite')  
print(df_ordinato.head())

# -------------------------------
# 8. Numero di vendite per città
# -------------------------------
vendite_per_citta = df['Città'].value_counts().sort_index()
print("\nNumero di vendite per città:")
print(vendite_per_citta)
