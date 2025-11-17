# ==========================================================
# CREAZIONE MATRICI
# ==========================================================

matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for riga in matrice:
    for elemento in riga:
        print(elemento)
        
# ==========================================================
# MATRICE FIORI
# ==========================================================

# Matrice che rappresenta il numero di petali di diversi fiori
# Righe: fiori (Rosa, Tulipano, Girasole)
# Colonne: stagioni (Primavera, Estate, Autunno)
petali = [
    [30, 32, 28],   # Rosa
    [6, 8, 5],      # Tulipano
    [20, 22, 18]    # Girasole
]

fiori = ["Rosa", "Tulipano", "Girasole"]
stagioni = ["Primavera", "Estate", "Autunno"]

# Stampa della matrice 
riga_index = 0
for riga in petali:
    print("\nNumero di petali del", fiori[riga_index], "nelle varie stagioni:")
    col_index = 0
    for elemento in riga:
        print(stagioni[col_index] + ":", elemento, "petali")
        col_index += 1
    riga_index += 1
