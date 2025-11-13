# ==========================================================
# TUPLE
# ==========================================================

""" # Creazione di alcune tuple: le tuple sono collezioni ordinate e immutabili
punto = (3, 4) 
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Femmina")

# Accesso agli elementi della tupla tramite l’indice (partendo da 0)
print(punto[0])  # stampa 3 (primo elemento)
print(punto[1])  # stampa 4 (secondo elemento)

# Creazione di una tupla senza parentesi tonde
punto = 3, 4

# "Unpacking" della tupla: assegna automaticamente i valori alle variabili x e y
x, y = punto 
print(x, y)  # stampa: 3 4

# ==========================================================
# INSIEMI (SET)
# ==========================================================

# Creazione di insiemi: i set sono collezioni non ordinate e senza duplicati
set1 = set([1, 2, 3, 4, 5])  # creazione usando la funzione set()
set2 = {4, 5, 6, 7, 8}       # creazione diretta con parentesi graffe
set3 = {1, 2, 3, 4, 4, 5}    # il numero 4 è duplicato ma verrà rimosso

print(set3)  # stampa: {1, 2, 3, 4, 5} (il duplicato è stato eliminato)

# Creazione di due insiemi per mostrare le principali operazioni matematiche
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Unione: tutti gli elementi di entrambi i set, senza duplicati
print(set1.union(set2))  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersezione: solo gli elementi comuni ai due set
print(set1.intersection(set2))  # {4, 5}

# Differenza: elementi che sono in set1 ma non in set2
print(set1.difference(set2))  # {1, 2, 3}

# Differenza simmetrica: elementi presenti in uno solo dei due set
print(set1.symmetric_difference(set2))  # {1, 2, 3, 6, 7, 8} """


# ==========================================================
# METODI PRINCIPALI DEGLI INSIEMI (SET)
# ==========================================================

#creazione insieme iniziale 
frutta = {"mela", "banana", "arancia"}
print("==========================================================") 
print("Insieme iniziale: ", frutta)
print("==========================================================") 

# 1. AGGIUNGERE un elemento con add()
frutta.add("kiwi")  # aggiunge un nuovo elemento

print("Dopo add('kiwi'):", frutta)
print("==========================================================") 

# 2. RIMUOVERE un elemento con remove()
frutta.remove("banana")  # rimuove 'banana' 
print("Dopo remove('banana'):", frutta)
print("==========================================================") 

# 3. RIMUOVERE un elemento con discard() 
frutta.discard("pera")  # non genera errore anche se 'pera' non è presente
print("Dopo discard('pera'):", frutta)
print("==========================================================") 

# 4. VERIFICARE la lunghezza con len() 
print("Numero di elementi nell'insieme:", len(frutta)) 
print("==========================================================") 

# 5. CONTROLLARE se un elemento è presente con 'in'
print("La mela è presente?", "mela" in frutta)  
print("La banana è presente?", "banana" in frutta)
print("==========================================================") 

# 6. CREARE UNA COPIA indipendente con copy()
copia_frutta = frutta.copy()
print("Copia dell'insieme:", copia_frutta)
print("==========================================================") 

# Se modifichi la copia, l'originale resta invariato
copia_frutta.add("pera")
print("Copia modificata:", copia_frutta)
print("Originale invariato:", frutta)