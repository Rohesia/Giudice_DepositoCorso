# ==========================================================
# LISTE
# ==========================================================

# Creazione di una lista di numeri interi
numeri = [1, 2, 3, 4, 5]  

# Creazione di una lista di stringhe (nomi)
nomi = ["Alice", "Bob", "Charlie"]  

# lista mista con tipi di dati diversi
misto = [1, "due", True, 4.5]  

# Accesso agli elementi della lista
#primo elemento della lista
print(numeri[0])   # Output: 1

#terzo elemento (indice 2)
print(numeri[2])   # Output: 3

#modifica di un elemento 
numeri[2] = 5
print(numeri)

# ==========================================================
# METODI DELLE LISTE
# ==========================================================

# Creiamo una lista di numeri
numeri = [3, 1, 4, 2, 5]

#len() -> restituisce la lunghezza della lista
print(len(numeri))  
# append() -> aggiunge un elemento alla fine della lista
numeri.append(6)     
print(numeri)        
# insert() -> inserisce un elemento in una posizione specifica
# Sintassi: lista.insert(indice, valore)
numeri.insert(2, 10)  
print(numeri)        # Output: [3, 1, 10, 4, 2, 5, 6]
# Inserisce il numero 10 alla posizione con indice 2 (terzo posto)
# remove() -> rimuove la prima occorrenza di un valore specificato
numeri.remove(4)      
print(numeri)        
#sort() -> ordina gli elementi della lista in ordine crescente
numeri.sort()         
print(numeri)    
