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
