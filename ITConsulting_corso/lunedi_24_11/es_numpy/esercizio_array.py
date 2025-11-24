import numpy as np

# 1. Creazione array di numeri interi da 10 a 49
arr = np.arange(10, 50)
print("array creato:", arr)

# 2. Verifica del tipo di dato (dtype)
print("Tipo di dato iniziale:", arr.dtype)

# 3. Conversione dell'array in float64
arr_float = np.array(arr, dtype=np.float64)
print("Tipo di dato dopo conversione a float:", arr_float.dtype)

# 4. Stampa della forma (shape) dell'array
print("Forma dell'array:", arr.shape)
