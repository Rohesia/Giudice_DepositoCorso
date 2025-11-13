
# ==========================================================
# Chiedere età
# ==========================================================

eta = int(input("Inserisci la tua età: "))
print("L'età che hai inserito è: ", eta)

print("\n------------------------------")
#controllo dell'età
if eta < 18:
    print("Mi dispiace, non puoi vedere questo film")
    print("Torna quando avrai 18 anni")
else:
    print("puoi vedere questo film")
    print("Buona visione")
    
print("------------------------------")


# ==========================================================
# CALCOLATRICE
# ==========================================================

print("==============================")
print(" CALCOLATRICE ")
print("==============================\n")

print("per eseguire le operazioni devi inserire almeno due numeri")

#chiedere all'utente di inserire i due numeri
numero1 = int(input("Inserisci il primo numero: "))
numero2 = int(input("Inserisci il secondo numero: "))

# operazioni 
operazione = input("scegli il tipo di operazione (+, -, *, /): ")
print("\n--------------------------------")


# match- case per le operazioni
match operazione:
    case "+":
        risultato = numero1 + numero2
        print(f"Risultato: {risultato}")
    case "-":
        risultato = numero1 - numero2
        print(f"Risultato: {risultato}")
    case "*":
        risultato = numero1 * numero2
        print(f"Risultato: {risultato}")
    case "/":
        if numero2 == 0:
            print("Errore: divisione per zero!")
        else:
            risultato = numero1 / numero2
            print(f"Risultato: {risultato}")
    case _:
        print("Operazione non valida.")

print("--------------------------------")