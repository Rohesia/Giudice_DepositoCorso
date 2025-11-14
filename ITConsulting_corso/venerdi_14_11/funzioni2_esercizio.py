# ==========================================================
# FUNZIONI - Esercizio 1
# ==========================================================

import random 

# Funzione saluto 
def saluto():
    print("Benvenuto in questo gioco")
    print("per vincere devi riuscire ad indovinare il numero corretto")
    print("se vuoi smettere di giocare inserisci 0.\n")
    
# Funzione per indovinare il numero 
def guess_number():
    numero = random.randint(1, 100)
    scelta = -1
    
    while scelta != numero:
        scelta = int(input("inserisci il numero: "))
        
        if scelta == 0:
            print("il gioco è terminato")
            break
        elif scelta < numero:
            print("il numero che hai scelto è troppo basso")
        elif scelta > numero:
            print("il numero che hai scelto è troppo alto")
        else: 
            print("Hai indovinato! Bravo")

# richiamo alla funzione
saluto()
guess_number()

# ==========================================================
# FUNZIONI - Esercizio 2
# ==========================================================

# sequenza di fibonacci fino ad un valore n 
def fibonacci(numero):
    a, b = 0, 1
    sequenza = []
    
    while a <= numero:
        sequenza.append(a)
        a, b = b, a + b
    return sequenza 

# stampa sequenza 
def stampa(sequenza):
    print("sequenza di fibonacci")
    print(sequenza)
    
# blocco principale
record = []

while True:
    numero = int(input("Inserisci un numero qualsiasi se vuoi uscire digita 0: "))
    
    if numero == 0:
        print("premendo 0, hai deciso di terminare il programma. Ecco tutte le sequenze generate:")
        print(record)
        break

    
    sequenza = fibonacci(numero)
    record.append(sequenza)
    stampa(sequenza)