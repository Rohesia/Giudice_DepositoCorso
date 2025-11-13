# ==========================================================
# Esercizio 1: Somma numeri con while
# ==========================================================

print("=== SOMMA DI NUMERI INTERI ===")

# inizializzo le variabili
somma = 0
conteggio = 0          
positivi = 0           
negativi = 0          

# ciclo infinito finché l'utente non inserisce 0
while True:
    numero = int(input("inserisci un numero intero (0 per terminare): "))
    
    # se l'utente inserisce 0,  il ciclo si interrompe
    if numero == 0:
        break 
    
    # aggiornamento di somma e conteggio
    somma += numero
    conteggio += 1
    
    # conteggio di numeri positivi e negativi
    if numero > 0:
        positivi += 1
    elif numero < 0:
        negativi += 1

# stampa dei risultati finali
print(f"\nLa somma totale dei numeri inseriti è: {somma}")
print(f"Hai inserito {conteggio} numeri in totale")
print(f"Numeri positivi: {positivi}")
print(f"Numeri negativi: {negativi}")


# ==========================================================
# Esercizio 2: Stampa lettere di una parola
# ==========================================================

print("=== STAMPA LETTERE DI UNA PAROLA ===")

# utente inserisce una parola
parola = input("inserisci una parola: ")

# inizializzo una stringa vuota dove concatenare le lettere
risultato = ""
numero_lettere = 0
vocali = "aeiouAEIOU"
conteggio_vocali = 0 
conteggio_consonanti = 0

# ciclo for per scorrere ogni lettera della parola
for lettera in parola:
    risultato += lettera + " "  # concateno la lettera per orizzontale
    numero_lettere += 1
    if lettera in vocali:
        conteggio_vocali += 1
    else: 
        conteggio_consonanti +=1
        
# stampo il risultato tutto insieme
print("\nLe lettere della parola sono:")
print(risultato)

#EXTRA
print(f"Numero totale di lettere: {numero_lettere}")
print(f"Numero di vocali: {conteggio_vocali}")
print(f"Numero di consonanti: {conteggio_consonanti}")

# ==========================================================
# Esercizio 3: Ciclo for con range
# ==========================================================

print("=== STAMPA NUMERI  ===")

numero = int(input("quanti numeri vuoi inserire? "))
# utente inserisce il numero massimo fino a cui stampare

step = int(input("inserisci lo step: "))
# step =  incremento ad ogni iterazione

print(f"\nNumeri da 0 a {numero} con passo {step}:")

for i in range(0, numero+1, step):
    print(i)

    