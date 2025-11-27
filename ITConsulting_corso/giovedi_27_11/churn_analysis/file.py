import pandas as pd 
import numpy as np 

df = pd.read_csv('telecom_customers_top.csv')

# info generali sul dataset 
print(df.head())
print(df.info())
print(df.describe())

# distribuzione della colonna target Churn 
print(df['Churn'].value_counts())

# --------------------------------------
# ----------- Pulizia dei dati ---------
# --------------------------------------

# valori mancanti 
print(df.isnull().sum())

# solo valori coerenti
df = df[(df['Età'] > 0) & 
        (df['Tariffa_Mensile'] > 0) & 
        (df['Dati_Consumati'] >= 0) & 
        (df['Durata_Abbonamento'] > 0) & 
        (df['Servizio_Clienti_Contatti'] >= 0)]

# colonne per analisi 
df['Costo_GB'] = df['Tariffa_Mensile'] / df['Dati_Consumati']

# creo un binning di età per fare l'abbonamento 
df['Età_bin'] = pd.cut(df['Età'], bins=[17, 30, 45, 60, 80], labels=['18-30','31-45','46-60','61-80'])
df['Durata_bin'] = pd.cut(df['Durata_Abbonamento'], bins=[0, 12, 36, 60, 120], labels=['0-12','13-36','37-60','61-120'])

# --------------------------------------
# ----------------- EDA ----------------
# --------------------------------------
# Analisi esplorativa 
# Churn medio per fascia di età
print(df.groupby('Età_bin')['Churn'].value_counts(normalize=True).unstack())

# Churn medio per fascia durata abbonamento
print(df.groupby('Durata_bin')['Churn'].value_counts(normalize=True).unstack())

# Correlazioni tra variabili numeriche
print(df[['Età','Durata_Abbonamento','Tariffa_Mensile','Dati_Consumati','Servizio_Clienti_Contatti','Costo_per_GB']].corr())

# per vederli faccio una pivot table 
pivot_churn = df.pivot_table(index='Età_bin', columns='Durata_bin', values='Churn', aggfunc=lambda x: (x=='Sì').mean())
print(pivot_churn)


