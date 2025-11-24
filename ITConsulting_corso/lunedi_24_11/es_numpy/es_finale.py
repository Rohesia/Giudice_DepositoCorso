import numpy as np 

print("="*70)
print("ESERCIZIO FINALE DAY ONE - NumPy")
print("="*70)

# ============================================================================
# 1. Creazione dell'array
# ============================================================================
print("\n[1] CREAZIONE ARRAY")
print("-"*70)

array = np.arange(0, 50)
array_casuale = np.random.randint(49, 102, size = 50)

fin_array = np.concatenate([array, array_casuale])

print(f"array finale: \n {fin_array}")
print(f"il tipo di array è: {fin_array.dtype}")
print(f"Shape dell'array: {array.shape}")

# ============================================================================
# 2. Conversione del dtype in float64
# ============================================================================
print("\n[2] CONVERSIONE DTYPE")
print("-"*70)

fin_array = np.array(fin_array, dtype=np.float64)
print("Tipo di dato dopo conversione a float:", fin_array.dtype)
print(f"Shape dell'array: {fin_array.shape}")

# ============================================================================ 
# 3. Slicing dell'array
# ============================================================================ 
print("\n[3] OPERAZIONI DI SLICING")
print("-"*70)

# Primi 10 elementi
el_10 = fin_array[:10]
print("Primi 10 elementi:")
print(el_10)

# Ultimi 7 elementi
ul_7 = fin_array[-7:]
print("\nUltimi 7 elementi:")
print(ul_7)

# Elementi dall'indice 5 all'indice 20 escluso
intervallo = fin_array[5:20]
print("\nElementi dall'indice 5 all'indice 19:")
print(intervallo)

# Ogni quarto elemento dell'array
el_4 = fin_array[::4]
print("\nOgni quarto elemento dell'array:")
print(el_4)

# ============================================================================ 
# 4. Modifica tramite slicing
# ============================================================================ 
print("\n[4] MODIFICA TRAMITE SLICING")
print("-"*70)

fin_array[10:15] = 999
print("Array dopo aver modificato gli elementi 10-14 a 999:")
print(fin_array)

# ============================================================================ 
# 5. Fancy indexing e maschere booleane
# ============================================================================ 
print("\n[5] FANCY INDEXING E MASCHERE BOOLEANE")
print("-"*70)

# elementi 
lista_el = [0, 3, 7, 12, 25, 33, 48]
el_posizioni = fin_array[lista_el]
print("Elementi in posizioni: ", el_posizioni)

# Elementi pari con maschera booleana
elementi_pari = fin_array[fin_array % 2 == 0]
print("Elementi pari dell'array:", elementi_pari)

# Elementi maggiori della media
media = fin_array.mean()
elementi_sopra_media = fin_array[fin_array > media]
print("Elementi maggiori della media dell'array:", elementi_sopra_media)

# ============================================================================ 
# 6. Stampa finale
# ============================================================================ 
print("\n[6] ARRAY FINALE E SOTTO-ARRAY")
print("-"*70)

print("Array finale dopo tutte le modifiche:")
print(fin_array)

print("\nSotto-array ottenuti tramite slicing e fancy indexing:")
print("Primi 10 elementi:", el_10)
print("Ultimi 7 elementi:", ul_7)
print("Elementi dall'indice 5 all'indice 20:", intervallo)
print("Ogni quarto elemento:", el_4)
print("Elementi selezionati:", el_posizioni)
print("Elementi pari:", elementi_pari)
print("Elementi sopra la media:", elementi_sopra_media)


