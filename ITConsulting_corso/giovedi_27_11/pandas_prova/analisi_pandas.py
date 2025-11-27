import pandas as pd 

# creazione di un DataFrame con dati di esempio 

data = {
    'Nome': ['Alice', 'Bob', 'Carla'],
    'Età': [25, 30, 22],
    'Città': ['Roma', 'Milano', 'Napoli']
}

df = pd.DataFrame(data)

# Stampa del DataFrame originale 
print("DataFrame originale: ")
print(df)

# selezione delle righe dove età è superiore a 23 
df_older = df[df['Eta'] > 23]

# Stampa delle righe selezionate

print("\nPersone con età superiore a 23 anni:")

print(df_older)


# Aggiungiamo una nuova colonna  la persona maggiorenne

df['Maggiorenne'] = df['Età'] >= 18


# Stampa del DataFrame con la nuova colonna

print("\nDataFrame con colonna 'Maggiorenne':")

print(df)