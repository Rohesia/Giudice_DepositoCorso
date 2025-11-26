import sqlite3
import os

# Nome del file database
db_filename = 'libreria_esempio.db'

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
CREATE TABLE IF NOT EXISTS libri (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titolo TEXT NOT NULL,
    autore TEXT NOT NULL,
    anno INTEGER,
    prezzo REAL
);
"""
cursor.execute(sql_create_table)
print("Tabella 'libri' creata con successo.")

# 4. INSERIMENTO DATI (INSERT) - Singolo
sql_insert = "INSERT INTO libri (titolo, autore, anno, prezzo) VALUES (?, ?, ?, ?)"
dati_libro = ("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 25.50)
cursor.execute(sql_insert, dati_libro)
print("Inserito un singolo libro.")

# 5. INSERIMENTO MULTIPLO (executemany)
lista_libri = [
    ("1984", "George Orwell", 1949, 12.00),
    ("Il Piccolo Principe", "Antoine de Saint-Exupéry", 1943, 9.50),
    ("Dune", "Frank Herbert", 1965, 18.90),
    ("Python Crash Course", "Eric Matthes", 2019, 35.00)
]
cursor.executemany(sql_insert, lista_libri)
print("Inserimento multiplo completato.")

# 6. COMMIT (salvataggio)
conn.commit()
print("Modifiche salvate nel database.")

# 7. LETTURA DATI (SELECT)
print("\n--- Lettura di tutti i libri ---")
cursor.execute("SELECT * FROM libri")
tutti_i_libri = cursor.fetchall()

for libro in tutti_i_libri:
    print(f"ID: {libro[0]} | Titolo: {libro[1]} | Prezzo: {libro[4]}€")

# 8. LETTURA FILTRATA E AGGIORNAMENTO PREZZO
print("\n--- Aggiornamento Prezzo per Orwell ---")
cursor.execute("SELECT id FROM libri WHERE autore = ?", ("George Orwell",))
id_orwell = cursor.fetchone()[0]

nuovo_prezzo = 15.00
cursor.execute("UPDATE libri SET prezzo = ? WHERE id = ?", (nuovo_prezzo, id_orwell))
conn.commit()
print(f"Prezzo aggiornato per il libro ID {id_orwell}.")

# 9. CANCELLAZIONE (DELETE)
print("\n--- Cancellazione libri vecchi ---")
cursor.execute("DELETE FROM libri WHERE anno < ?", (1950,))
print(f"Cancellati {cursor.rowcount} libri pubblicati prima del 1950.")
conn.commit()

# 10. STAMPA PERCORSO ASSOLUTO DEL DB
print("\nPercorso completo del file DB:")
print(os.path.abspath(db_filename))
