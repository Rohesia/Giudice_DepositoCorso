
# ==========================================================
# ESERCIZIO 1 BASE
# ==========================================================


while True:
    scelta = input("Vuoi inserire un numero o una stringa? (n/s): ").lower()
    
    #scelta di un numero
    if scelta == "n":
        numero = int(input("inserisci un numero: "))
        
        #controllo pari o dispari 
        if numero % 2 == 0:
            print(f"il numero {numero} è pari")
        else: 
            print(f"il numero {numero} è dispari")
    
    #scelta della stringa 
    elif scelta == "s":
        testo = input("inserisci una stringa: ")
        print(f"Hai scritto: {testo}")
        lunghezza = len(testo)
        print(f"La stringa contiene {lunghezza} lettere.")
        
        # controllo se il numero di lettere è pari o dispari
        if lunghezza % 2 == 0:
            print("Il numero di lettere è PARI.")
        else:
            print("Il numero di lettere è DISPARI.")
        
        
    else: 
        print("puoi scegliere solo s per stringa ed n per numero")
        
    # continuare o meno il ciclo 
    ripetere = input("vuoi ripetere? (s/n)").lower()
    if ripetere != "s":
        print("programma terminato")
        break
    
# ==========================================================
# ESERCIZIO 2 INTERMEDIO
# ==========================================================

while True:
    print("NUMERI PRIMI IN UN INTERVALLO")
    
    inizio = int(input("inserisci il numero iniziale: "))
    fine = int(input("inserisci il numero finale: "))
    
    #creazione di due liste
    numeri_primi = []
    numeri_non_primi = []
    
    for numero in range(inizio, fine +1):
        if numero < 2:
            numeri_non_primi.append(numero)
            
        else: 
            
            primo = True 
            
            for i in range(2, int(numero**0.5) + 1):
                if numero % i == 0:
                    primo = False 
                    break 
            if primo:
                numeri_primi.append(numero)
            else: 
                numeri_non_primi.append(numero)
    
    print("\n Numeri primi trovati: ", numeri_primi)
    print("\n Numeri non primi trovati: ", numeri_non_primi)
    
    #ripetizione 
    ripetizione = input("vuoi ripetere?(s/n): ").lower()
    if ripetizione!= "s":
        print("programma terminato")
        break