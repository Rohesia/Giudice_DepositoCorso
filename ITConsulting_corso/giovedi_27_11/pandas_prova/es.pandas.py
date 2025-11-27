import pandas as pd

# ppercorso del csv 
file_path = 'vendite.csv'

# caricamento dati nel DataFrame 
df = pd.read_csv(file_path)

# le prme righe del DataFrame per confermare 
print(df.head())