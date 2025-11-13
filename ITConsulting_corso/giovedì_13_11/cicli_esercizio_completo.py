
# ==========================================================
# USO di if
# ==========================================================

#chiedere all'utente un numero 
numero = int(input("inserisci un numero: "))

if numero % 2 == 0:
    print(f"{numero} è pari")
else:
    print(f"{numero} è dispari")
    

# ==========================================================
# USO di while e range
# ==========================================================

numero = int(input("Inserisci un numero: "))

if numero < 0:
    print("il numero che hai inserito deve essere positivo")
else: 
    for i in range(numero, -1, -1): # da numero a 0, decrementa di 1
        print(i)
        
# ==========================================================
# USO di for
# ==========================================================

numeri = []

n = int(input("quanti numeri vuoi inserire nella lista? "))

# ciclo per inserire i numeri nella lista 
for i in range(n):
    numero = int(input(f"inserisci il numero nella lista {i+1}: "))
    numeri.append(numero)
    
print(numeri)
    
# stampa del quadrato di ciascun numero
for numero in numeri:
    print(f"Il quadrato di {numero} è {numero**2}")
    
# ==========================================================
# USO di if, while, for
# ==========================================================

lista_numeri = []

n = int(input("quanti numeri vuoi inserire? "))

# inserimento dei numeri nella lista 
for i in range(n):
    numero = int(input(f"inserisci il numero {i+1}: "))
    lista_numeri.append(numero)
    

# PUNTO IF controllo che la lista non sia vuota 
if len(lista_numeri) == 0:
    print("la lista è vuota")
else: 
    # PUNTO FOR per trovare il massimo 
    massimo = lista_numeri[0]
    for numero in lista_numeri:
        if numero > massimo:
            massimo = numero 
            
    #Punto WHILE: conteggio dei numeri presenti
    count = 0 
    i = 0 
    while i < len(lista_numeri):
        count += 1
        i +=1
    
    # stampa del risultato
    print(f"Numero massimo: {massimo}")
    print(f"Numero di elementi nella lista: {count}")
