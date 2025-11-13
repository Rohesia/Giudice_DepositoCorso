
while True:
    numero = int(input("inserisci un numero: "))
   
    # conto alla rovescia
    for i in range(numero, -1, -1):   # parte da numero, e arriva a 0 incluso
        print(i)
        
    risposta = input("vui ripetere? (s/n)").lower()
    if risposta != "s":
        print("programma terminato")
        break
    
# numeri primi 
# lista numeri primi 
numeri_primi = []

while len(numeri_primi) < 5:
    # inserisci numero
    numero = int(input("Inserisci numero: "))
    
    # controlliamo se il numero è valido (>=2)
    if numero >= 2:
        primo = True # assumo che il numero sia primo
        i = 2 
        while i < numero:
            if numero % i == 0:
                primo = False
            i += 1 #provo a passare al prossimo divisore
        
        if primo:
            numeri_primi.append(numero)
            print(f"{numero} è primo! Lista salvata: {numeri_primi}")
        else:
            print(f"{numero} non è primo")
    else:
        print(f"{numero} non è primo")

print("Sono stati inseriti 5 numeri primi!")