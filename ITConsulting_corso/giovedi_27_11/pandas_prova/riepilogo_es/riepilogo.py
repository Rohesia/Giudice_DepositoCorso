import pandas as pd 

# -----------------------------------
# ----- Caricamento del dataset -----
# -----------------------------------

dataset = pd.read_csv('titanic.csv')

# stampa delle ultime 5 righe e delle prime 5 righe 
""" 
prime_5_righe = dataset.iloc[:5]
ultime_5_righe = dataset.iloc[-5:] 
"""

print(dataset.head())
print(dataset.tail())

# visualizzazione del tipo di dato di ciascuna colonna 
tipi_di_dati = dataset.dtypes
print(tipi_di_dati)

# Selezioniamo solo le colonne numeriche
""" colonne_numeriche = dataset.select_dtypes(include='number')
print("Media:\n", colonne_numeriche.mean())
print("Mediana:\n", colonne_numeriche.median())
print("Deviazione standard:\n", colonne_numeriche.std())
 """
print(dataset.describe())

# -----------------------------------------
# --------- Pulizia dei dati --------------
# -----------------------------------------
# rimozione duplicati
dataset = dataset.drop_duplicates()

# gestione dei valori mancanti 
def valori_mancanti(df):
    for col in df.select_dtypes(include='number').columns:
        df[col].fillna(df[col].median(), inplace=True)
    return df

dataset = valori_mancanti(dataset)

#------------- colonna età --------------
# aggiungere colonna categoria età 
def categoria_eta(age):
    if age <= 18:
        return "Giovane"
    elif age <= 65:
        return "Adulto"
    else:
        return "Senior"

dataset['Categoria Età'] = dataset['Age'].apply(categoria_eta)

# ------------ Salvataggio CSV ----------
dataset.to_csv('titanic_pulito.csv', index=False)

# Stampa finale
print("\nDataset aggiornato con Categoria Età:")
print(dataset.head())