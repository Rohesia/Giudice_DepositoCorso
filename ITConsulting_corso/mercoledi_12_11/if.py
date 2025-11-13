""" # ==========================================================
# Esercizio 1: Controllo annidato a 3 livelli
# ==========================================================

ingrediente = input("dimmi l'ingrediente principale: ")

# Primo livello di controllo 
if ingrediente == "farina":
    print("ingrediente corretto al primo livello")
    
    #secondo livello 
    liquido = input("dimmi un liquido da usare: ")
    if liquido == "latte":
        print("hai superato il secondo livello")
        
        #terzo livello 
        quantita = int(input("dimmi il numero di uova da usare: "))
        if quantita == "2":
            print("accesso consentito: ricetta approvata")
        else:
            print("quantita sbagliata")
    else:
        print("liquido non corretto")
else:
    print("Ingrediente principale sbagliato: accesso negato") """
    
# ==========================================================
# Esercizio 2: Menu CRUD
# ==========================================================

# definire le variabili 
""" elemento1 = "Mela"
elemento2 = "Banana"
elemento3 = "Arancia"

#Menu CRUD
print("==========================================================")
print("Menu CRUD")
print("==========================================================")
print("A - Aggiungi")
print("R - Rimuovi")
print("V - Visualizza")
print("E - Esci")

#scelta
scelta = input("scegli un'opzione")

if scelta == "A" or scelta == "a":
    # Aggiungi o modifica un elemento
    n = input("Quale elemento vuoi cambiare? (1, 2 o 3): ")
    nuovo_valore = input("Inserisci il nuovo valore: ")
    
    if n == "1":
        elemento1 = nuovo_valore
    elif n == "2":
        elemento2 = nuovo_valore
    elif n == "3":
        elemento3 = nuovo_valore
    else:
        print("Numero non valido")
    
    print("Elementi aggiornati:", elemento1, elemento2, elemento3)

elif scelta == "R" or scelta == "r":
    # Rimuovi un elemento
    n = input("Quale elemento vuoi rimuovere? (1, 2 o 3): ")
    
    if n == "1":
        elemento1 = ""
    elif n == "2":
        elemento2 = ""
    elif n == "3":
        elemento3 = ""
    else:
        print("Numero non valido")
    
    print("Elementi aggiornati:", elemento1, elemento2, elemento3)

elif scelta == "V" or scelta == "v":
   
    print("Elementi correnti:", elemento1, elemento2, elemento3)

elif scelta == "E" or scelta == "e":
    
    print("Uscita dal menu")

else:
    # Input non valido
    print("Opzione non valida, riprova") """
    

# ==========================================================
# Esercizio 3: Creazione e controllo account semplice
# ==========================================================

#variabile account esistente
utente = "Alice"
password_ex = "1234"
id = 1

# nuovo id
id_1 = 2

#registrazione
scelta = input("vuoi registrarti? (si/no)")

if scelta.lower == "si":
    nome = input("inserisci il nome")
    password = input("inserisci password")
    
    user_id = id_1
    id_1 += 1
    
    #print dei dati
    print(f"Account creato! Nome: {nome}, Password: {password}, ID: {user_id}")

else:
    nome = input("inserisci il nome")
    password = input("inserisci password")
    
    if nome == utente and password == password_ex:
        print(f"Accesso consentito! ID utente: {id}")
    else:
        print("Utente non trovato o password errata. Termino lo script.")
        exit()