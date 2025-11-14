# ==========================================================
# Esercizio
# ==========================================================

#creazione di una lista vuota
lista_numeri = []

while True: 
    # 1. chiedere all'utente di inserire un numero positivo
    numero = int(input("Inserisci un numero intero e positivo: "))
    while numero <= 0:
        print("Il numero che devi inserire deve essere positivo!")
        numero = int(input("Inserisci un numero intero e positivo: "))

    # inserire il numero nella lista
    lista_numeri.append(numero)
    
    #stampa della lista
    print(f"lista dei numeri attualmente presenti: {lista_numeri}")

    # 2. somma dei numeri pari
    somma_numeri_pari = 0
    for i in range(1, numero + 1):
        if i % 2 == 0:
            somma_numeri_pari += i
    print(f"La somma dei numeri pari da 1 a {numero} è: {somma_numeri_pari}")

    # 3. stampa dei numeri dispari
    print(f"Numeri dispari da 1 a {numero}:")
    for i in range(1, numero + 1):
        if i % 2 != 0:
            print(i, end=" ")
    print() 

    # 4. verifica se il numero è primo
    print("==========================================================")
    print(" ======== VERIFICA NUMERO PRIMO ==========")
    print("==========================================================")

    if numero < 2:
        print(f"{numero} NON è un numero primo")
    else:
        primo = True
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                primo = False
                break
        if primo:
            print(f"{numero} è un numero primo")
        else:
            print(f"{numero} NON è un numero primo")

    # ripetizione del programma
    ripetizione = input("Vuoi ripetere? (s/n): ").lower()
    if ripetizione != "s":
        print("Programma terminato")
        break
