# Stampa di Hello a schermo
print("Hello")  

# Creazione di variabili con diversi tipi di dato 
nome = 'Rosy'                        # stringa 
altezza = 1.65                        # float 
titoloStudio = "Laurea in ingegneria Informatica"  # stringa

'''
Stampiamo tutte le informazioni insieme usando print
La virgola separa i valori e Python li stampa con uno spazio tra loro
'''
print(f"Ciao mi chiamo", nome, "sono alta: ", altezza, "il mio titolo di studio:", titoloStudio)

# Con la funzione input l'utente inserirà il suo nome
nome = input("inserisci il tuo nome: ")  

# Chiediamo all'utente di inserire la sua età e la convertiamo in numero intero
eta = int(input("dimmi la tua eta:"))  # casting

# Stampiamo un messaggio di benvenuto personalizzato
# Qui usiamo la concatenazione con il simbolo + per unire testo e variabile
print("Ciao: " + nome + " " + "Benvenuto in Python!")

# Esempi di operazioni matematiche semplici
print(1+2)   # somma: stampa 3
print(10-5)  # sottrazione: stampa 5
