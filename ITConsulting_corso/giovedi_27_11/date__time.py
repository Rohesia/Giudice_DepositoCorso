import pandas as pd
import numpy as np

# ------------------------------
# 1. Dataset semplice
# ------------------------------
np.random.seed(42)
date_range = pd.date_range(start="2025-11-01", end="2025-11-10", freq='D')
vendite = np.random.randint(50, 500, size=len(date_range))

df = pd.DataFrame({'date': date_range, 'vendite': vendite})
df.set_index('date', inplace=True)

print("DataFrame originale:")
print(df)

# ------------------------------
# 2. Aggregazioni temporali
# ------------------------------
df_daily = df.resample('D').mean()  # media giornaliera
df_monthly = df.resample('M').sum() # somma mensile

print("\nMedia giornaliera:")
print(df_daily)
print("\nSomma mensile:")
print(df_monthly)

# ------------------------------
# 3. Analisi avanzata
# ------------------------------
# Valore del giorno precedente
df['prev_day'] = df['vendite'].shift(1)

# Tasso di variazione giornaliero
df['daily_return'] = df['vendite'].pct_change()

# Rolling window di 7 giorni: media e deviazione standard
df['rolling_mean7'] = df['vendite'].rolling(window=7).mean()
df['rolling_std7']  = df['vendite'].rolling(window=7).std()

print("\nDataFrame con analisi avanzata:")
print(df)
