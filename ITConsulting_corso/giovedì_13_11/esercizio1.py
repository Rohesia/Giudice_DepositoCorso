# ==========================================================
# CALCOLATRICE
# ==========================================================

print("==============================")
print(" CALCOLATRICE ")
print("==============================\n")

print("per eseguire le operazioni inserisci i numeri richiesti")
print(" ")


#chiedere all'utente di inserire i numeri
print("\n--------------------------------")
numero1 = int(input("Inserisci il primo numero: "))
print("\n--------------------------------")
numero2 = int(input("Inserisci il secondo numero: "))
print("\n--------------------------------")
numero3 = int(input("Inserisci il terzo numero: "))
print("\n--------------------------------")
numero4 = int(input("Inserisci il quarto numero: "))

print(" ")
lista_numeri = [numero1, numero2, numero3, numero4]
print(" ")

print("\n--------------------------------")
#controllo di numeri positivi
if numero1 > 0 and numero2 > 0 and numero3 > 0 and numero4 > 0:
    lista_numeri.sort()
    print("i numeri sono positivi")
else: 
    print("ci sono numeri negativi, la lista non verrà ordinata.")
    print("\n--------------------------------")

print(f"Lista di numeri: {lista_numeri}")
print("\n--------------------------------")


# operazioni 
operazione = input("scegli il tipo di operazione (+, -, *, /): ")
print("\n--------------------------------")


# match- case per le operazioni
match operazione:
    case "+":
        risultato = numero1 + numero2 + numero3 + numero4
        print(f"Risultato: {risultato}")
    case "-":
        risultato = numero1 - numero2 - numero3 - numero4
        print(f"Risultato: {risultato}")
    case "*":
        risultato = numero1 * numero2 * numero3 * numero4
        print(f"Risultato: {risultato}")
    case "/":
        if numero2 == 0 or numero3 == 0 or numero4 == 0:
            print("Errore: divisione per zero!")
        else:
            risultato = numero1 / numero2 / numero3 / numero4
            print(f"Risultato: {risultato}")
    case _:
        print("Operazione non valida.")

print("--------------------------------")