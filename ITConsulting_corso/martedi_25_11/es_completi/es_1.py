import numpy as np

# 1. Creare un array di 15 numeri casuali tra 1 e 100
arr = np.random.randint(1, 101, size=15) 

print("Array:", arr)

# 2. Calcolare la somma di tutti gli elementi
somma = np.sum(arr)
print("Somma degli elementi:", somma)

# 3. Calcolare la media di tutti gli elementi
media = np.mean(arr)
print("Media degli elementi:", media)
