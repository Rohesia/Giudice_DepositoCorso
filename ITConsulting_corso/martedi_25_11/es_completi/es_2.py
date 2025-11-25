# esercizio 2
import numpy as np 

# matrice di valori 1, 25 con dimensione 5x5
mat = np.arange(1, 26).reshape(5, 5)
print("Matrice 5x5:\n", mat)

# Estrarre seconda colonna
colonna_2 = mat[:, 1]
print("Seconda colonna:", colonna_2)

# Estrarre terza riga
riga_3 = mat[2, :]
print("Terza riga:", riga_3)

# Estrarre la diagonale principale
diag = np.diag(mat)
print("Diagonale principale:", diag)

# Somma della diagonale
somma_diag = np.sum(diag)
print("Somma della diagonale principale:", somma_diag)
