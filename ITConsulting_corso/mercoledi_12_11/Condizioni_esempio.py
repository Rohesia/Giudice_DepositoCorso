# ==========================================================
# Esercizio 1: Controllo condizionale semplice
# ==========================================================

# Inizializzazione della variabile
numero = 10  # viene assegnato il valore 10 alla variabile 'numero'

# Controllo condizionale con if
if numero > 0:
    # Se la condizione è vera (numero > 0), viene eseguito questo blocco
    print("il numero è positivo")  

# ==========================================================
# Esercizio 2: Controllo condizionale con if-else
# ==========================================================

# Inizializzazione di una nuova variabile
numero = -1  # assegno un valore negativo 

# Controllo condizionale con if e else
if numero > 0:
    # Questo blocco viene eseguito solo se numero > 0
    print("il numero è positivo")
else:
    # Se la condizione dell'if non è vera, viene eseguito questo blocco
    print("Blocco Else") 

# ==========================================================
# Esempio: if annidato
# ==========================================================

# Definiamo una variabile
numero = 5

# Primo controllo
if numero > 0:
    print("Il numero e positivo")
    
    # Controllo annidato: se il numero è anche maggiore di 10
    if numero > 10:
        print("Il numero e maggiore di 10")
    else:
        print("Il numero e positivo ma minore o uguale a 10")
        
# Se non viene rispettata la condizione
else:
    print("Il numero non è positivo")


# ==========================================================
# Esempio: MATCH
# ==========================================================

comando = input("inserisci un comando: ")

match comando:
    case "start":
        print("avvio del programma")
    case "stop":
        print("chiusura del programma")
    case "pausa":
        print("programma in pausa")
    case _:
        print("comando non riconosciuto")