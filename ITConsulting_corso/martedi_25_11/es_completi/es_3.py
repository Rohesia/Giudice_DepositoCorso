# esercizio 3
import numpy as np 

# Creare array 4x4 di numeri casuali tra 10 e 50, con 50 escluso , quindi da 10 a 49
arr = np.random.randint(10, 50, size=(4,4))
print("Array iniziale:\n", arr)

# Fancy indexing per selezionare elementi
righe = np.array([0, 1, 2, 3])
colonne = np.array([1, 3, 2, 0])
el = arr[righe, colonne]
print("Elementi selezionati:", el)

# array di indici per numeri dispari
""" indici = np.arange(arr.shape[0])
disp = indici % 2 == 1
disp_r = arr[disp, :] """

# Righe dispari
disp_r = arr[1::2, :]
print("Righe dispari:\n", disp_r)

# Aggiungere 10 agli elementi selezionati (broadcasting)
arr[righe, colonne] += 10
print("Array con aggiunta del valore 10 agli elementi selezionati:\n", arr)
