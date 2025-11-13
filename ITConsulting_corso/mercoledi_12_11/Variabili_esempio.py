# ==========================================================
# Esercizio 1: Numeri interi (int) e stampa
# ==========================================================

# Inizializzazione di due variabili di tipo intero
x = 7   # il valore 7 è assegnato alla variabile x
y = 8   # il valore 8 è assegnato alla variabile y

# Stampiamo i valori delle due variabili
print(x, y)

# ==========================================================
# Esercizio 2: Numeri decimali (float) e stampa
# ==========================================================

# variabili di tipo float
altezza = 1.65     
peso = 55.5         
pi = 3.14159        

# Stampiamo i float singolarmente
print(altezza)      # Output: 1.65
print(peso)         # Output: 55.5
print(pi)           # Output: 3.14159

# Stampa dei valori
print("Altezza:", altezza, "Peso:", peso, "Pi:", pi)

# ==========================================================
# Esercizio 3: Stringhe - accesso ai caratteri
# ==========================================================

s = "Python"  # creazione della stringa

# Stampa il primo carattere della stringa (indice 0)
print(s[0])  # Output: "P"

# Stampa il terzo carattere della stringa (indice 2)
print(s[2])  # Output: "t"

# ==========================================================
# Esercizio 4: Concatenazione di stringhe
# ==========================================================

saluto = "Ciao"
nome = "Alice"

# Uniamo due stringhe con uno spazio in mezzo
messaggio = saluto + " " + nome
print(messaggio)  # Output: "Ciao Alice"

# ==========================================================
# Esercizio 5: Funzionalità delle stringhe
# ==========================================================

s = "Ciao, mondo!"

# Restituisce la lunghezza della stringa (numero di caratteri)
print(len(s))  # Output: 12

# Trasforma tutti i caratteri in maiuscolo
print(s.upper())  # Output: "CIAO, MONDO!"

# Divide la stringa in una lista usando la virgola come separatore
print(s.split(','))  # Output: ['Ciao', ' mondo!']

# Sostituisce una parte della stringa con un'altra
print(s.replace('mondo', 'universo'))  # Output: "Ciao, universo!"

# ==========================================================
# Esercizio 6: Singolo carattere
# ==========================================================

carattere = 'A'  # una variabile contenente un singolo carattere
print(carattere) # Output: "A"

# ==========================================================
# Esercizio 7: Booleani e logica
# ==========================================================

# Creazione di variabili booleane
vero = True       
falso = False     

# Stampiamo i valori booleani
print(vero)       # Output: True
print(falso)      # Output: False

# ==========================================================
# Esercizio 8: Operatori logici (and, not)
# ==========================================================

# Definiamo tre variabili intere
x = 5
y = 10
z = 7

# Operatore logico "and": True solo se entrambe le condizioni sono vere
print(x < y and y > z)  # True
print(x < y and z > y)  # False

# Operatore logico "not": inverte il valore booleano
print(not(x < y))        # False

# ==========================================================
# Esercizio 9: Operatori di confronto
# ==========================================================

x = 5
y = 10

# Controlli di uguaglianza e confronto
print(x == y)  # False, perché 5 non è uguale a 10
print(x != y)  # True, perché 5 è diverso da 10
print(x < y)   # True, perché 5 è minore di 10
