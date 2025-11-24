# Funzione che controlla se un numero è pari
def is_even(x):
    # Restituisce True se x è divisibile per 2, altrimenti False
    return x % 2 == 0

# Lista di numeri da 1 a 10
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Applica la funzione is_even a tutti gli elementi della lista
# filter mantiene solo gli elementi per cui is_even ritorna True
even_numbers = list(filter(is_even, numbers))

# Stampa la lista dei numeri pari filtrati
print(even_numbers) 


#--------------------------------------
# Esercizio filtro 
#--------------------------------------

numbers = [1, 4, 2, 1, 7, 5, 8]

filtered = []

# Iteriamo su tutti gli elementi tranne gli ultimi due
for i in range(len(numbers)):
    # Calcolo di i+1 e i+2
    first = numbers[i]
    second = numbers[i+1] if i+1 < len(numbers) else numbers[i]        
    third = numbers[i+2] if i+2 < len(numbers) else numbers[i+1]     

    # Condizione: i primi due numeri devono essere > del terzo
    if first > third and second > third:
        filtered.append(first)

print(filtered)
