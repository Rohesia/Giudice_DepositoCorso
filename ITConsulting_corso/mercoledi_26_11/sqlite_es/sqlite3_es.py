import sqlite3
import os
from utils import *
from analisi import *


# 1. prendo i dati dal file intestazione con i diversi dati associati
headers, dati = carica_csv("california_housing_data.csv")

# 2. pulizia dei dati da outlier e nan
dati = rimuovi_nan(dati)
dati = rimuovi_outlier(dati)

# Nome del file database
db_filename = 'california.db'

# Rimuovo il file se esiste già per avere un ambiente pulito ad ogni esecuzione
if os.path.exists(db_filename):
    os.remove(db_filename)

# 1. CREAZIONE E CONNESSIONE
print(f"--- Connessione a {db_filename} ---")
conn = sqlite3.connect(db_filename)

# 2. CREAZIONE DEL CURSORE
cursor = conn.cursor()

# 3. CREAZIONE TABELLA (DDL)
sql_create_table = """
CREATE TABLE IF NOT EXISTS california_housing (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    MedInc REAL,
    HouseAge REAL,
    AveRooms REAL,
    AveBedrms REAL,
    Population REAL,
    AveOccup REAL,
    Latitude REAL,
    Longitude REAL,
    MedHouseVal REAL
)
"""
cursor.execute(sql_create_table)
conn.commit()


sql_insert = """
INSERT INTO california_housing 
(MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude, MedHouseVal)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

# Trasformo i dati in tuple
dati_tuple = [tuple(riga) for riga in dati]

# Inserimento dati nel DB
cursor.executemany(sql_insert, dati_tuple)
conn.commit()

print(f"Inseriti {cursor.rowcount} record nel database.")
conn.close()

# ========================================
# ======== CREAZIONE DEL SECONDO DB ======
# ========================================

import sqlite3
import os
from analisi import posizione_misura

# Nome secondo database
db_risultati = 'california_risultati.db'
if os.path.exists(db_risultati):
    os.remove(db_risultati)

conn_risultati = sqlite3.connect(db_risultati)
cursor_risultati = conn_risultati.cursor()

# Creazione tabella risultati
sql_create = """
CREATE TABLE IF NOT EXISTS risultati (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    variabile TEXT,
    minimo REAL,
    massimo REAL,
    media REAL,
    mediana REAL,
    deviazione REAL
)
"""
cursor_risultati.execute(sql_create)
conn_risultati.commit()

# Calcolo le statistiche sui dati puliti
stats = posizione_misura(dati)

# Preparo i dati per l'inserimento
dati_risultati = []
for i, col in enumerate(headers):
    dati_risultati.append((
        col,
        stats['min'][i],
        stats['max'][i],
        stats['mean'][i],
        stats['median'][i],
        stats['std'][i]
    ))

# Inserimento nel database
sql_insert = """
INSERT INTO risultati 
(variabile, minimo, massimo, media, mediana, deviazione)
VALUES (?, ?, ?, ?, ?, ?)
"""
cursor_risultati.executemany(sql_insert, dati_risultati)
conn_risultati.commit()
print(f"Inseriti {cursor_risultati.rowcount} record nel database dei risultati ({db_risultati}).")

# Lettura dei dati dal DB dei risultati
cursor_risultati.execute("SELECT * FROM risultati")
for row in cursor_risultati.fetchall():
    print(row)


