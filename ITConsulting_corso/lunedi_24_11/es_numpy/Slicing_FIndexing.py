import numpy as np

# --- 1. array di 20 numeri casuali tra 10 e 50 ---
arr = np.random.randint(10, 51, size=20)
print("array originale:")
print(arr)

# --- 2. primi 10 elementi ---
arr_primi_10 = arr[:10]
print("\nI primi 10 elementi dell'array sono:")
print(arr_primi_10)

# --- 3. ultimi 5 elementi ---
arr_ultimi_5 = arr[-5:]
print("\nGli ultimi 5 elementi dell'array sono:")
print(arr_ultimi_5)

# --- 4. elementi dall'indice 5 all'indice 15 (escluso) ---
arr_intervallo = arr[5:15]
print("\nGli elementi dall'indice 5 all'indice 15 sono:")
print(arr_intervallo)

# --- 5. ogni terzo elemento dell'array ---
arr_terzo = arr[::3]
print("\nOgni terzo elemento dell'array è:")
print(arr_terzo)

# --- 6. Modifica di elementi dall'indice 5 all'indice 10 ---
arr[5:10] = 99
print("\nArray modificato: ora gli elementi dall'indice 5 all'indice 9 valgono 99")
print(arr)


# ---------------------------------
# Matrice 
# ---------------------------------

# matrice di numeri casuali tra 10 e 50
matrice = np.random.randint(10, 51, size=(4, 5))
print("\nMatrice originale 4x5:")
print(matrice)

# prime due righe 
indici_righe = [0, 1]
righe_iniziali = matrice[indici_righe, :]
print("\nPrime due righe (fancy indexing):")
print(righe_iniziali)

# ultime colonne
indici_colonne = [3, 4]
colonne_finali = matrice[:, indici_colonne]
print("\nUltime due colonne (fancy indexing):")
print(colonne_finali)

# Sottoarray centrale
righe_sottoarray = [1, 2]
colonne_sottoarray = [1, 2, 3]
sottoarray = matrice[np.ix_(righe_sottoarray, colonne_sottoarray)]
print("\nSottoarray centrale:")
print(sottoarray)

# Modifica 
matrice[np.ix_(righe_sottoarray, colonne_sottoarray)] = 99
print("\nMatrice modificata (sottoarray diventano 99):")
print(matrice)

# ---------------------------------
# Matrice 6 * 6
# ---------------------------------


# --- 1. Creazione di una matrice 6x6 di numeri casuali tra 1 e 100 ---
mat = np.random.randint(1, 101, size=(6, 6))
print("Matrice originale:")
print(mat)

# --- 2. Estrazione della sotto-matrice centrale ---
s_mat = mat[1:5, 1:5]
print("\nSotto-matrice centrale:")
print(s_mat)

# --- 3. Inversione delle righe della sotto-matrice ---
mat_inv = s_mat[::-1, :]
print("\nSotto-matrice con righe invertite:")
print(mat_inv)

# --- 4. Estrazione della diagonale principale ---
diagonale = np.diag(mat_inv)
print("\nDiagonale principale:")
print(diagonale)

# --- 5. Sostituzione degli elementi multipli di 3 con -1 ---
mod = mat_inv.copy()  
mod[mod % 3 == 0] = -1
print("\nMatrice invertita con multipli di 3 sostituiti da -1:")
print(mod)
