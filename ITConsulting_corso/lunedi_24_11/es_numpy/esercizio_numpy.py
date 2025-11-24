import numpy as np 
# esempio 1 
# creazione di un array unidimensionale 
arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)

# creazione di un array bidimensionale 
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d.shape)

# esempio 2
arr = np.array([1, 2, 3, 4, 5])

print("Forma dell'array: ", arr.shape)
print("Dimensione dell'array: ", arr.ndim)
print("Tipo di dato: ", arr.dtype)
print("Numero di elementi: ", arr.size)
print("Somma degli elementi: ", arr.sum())
print("Media degli elementi: ", arr.mean())
print("Valore massimo: ", arr.max())
print("Indice del valore massimo: ", arr.argmax())


# esempio 3
arr = np.array([[1, 2], [3, 4, 5]], dtype=object)
print(arr)

# esempio 4
arr = np.arange(10)
print(arr)

#esempio 5 
arr = np.arange(6)
reshaperd_arr = arr.reshape((2, 3))
print(reshaperd_arr)

# esempio 6
arr = np.array([1, 2, 3, 4, 5])

#Indexing
print(arr[0])

#Slicing
print(arr[1:3])

# Boolean Indexing 
print(arr[arr > 2])

# ----------------------------
# Indexing e Slicing 
# ----------------------------

arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])
# slicing su righe 
print(arr_2d[1:3])

#slicing su colonne 
print(arr_2d[:, 1:3])

# slicing misto 
print(arr_2d[1: , 1:3])

# ----------------------------
# Slicing 
# ----------------------------

# slicing con passo 
print(arr[1:8:2]) 

# omettere start e stop 
print(arr[:5])
print(arr[5:])

# usare indici negativi 
print(arr[-5:])
print(arr[:-5])

# ----------------------------
# Fancy Indexing
# ----------------------------
arr = np.array([10, 20, 30, 40, 50])

#  uso di array di indici 
indices = np.array([1, 3])
print(arr[indices])

# uso di una lista di indici 
indices = [0, 2, 4]
print(arr[indices])