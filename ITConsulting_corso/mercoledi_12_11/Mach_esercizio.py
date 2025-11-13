# ==========================================================
# LOGIN 
# ==========================================================

# Credenziali predefinite
nome_utente = "admin"
password_utente = "12345"

# 1. Input dell'utente
nome = input("Inserisci nome utente: ")
password = input("Inserisci password: ")

# 2. Verifica delle credenziali
if nome == nome_utente and password == password_utente:
    print("\n Accesso riuscito! Benvenuto", nome)

    # 4. Modifica del dato
    modifica = input("Vuoi cambiare la tua password? (s/n): ")
    if modifica.lower() == "s":
        nuova_password = input("Inserisci la nuova password: ")
        password_utente = nuova_password
        print(" Password aggiornata!")
    else:
        print("La password resta invariata.")

    # 4. Domande segrete 
    print("\nScegli una domanda segreta:")
    print("1 - Qual è il tuo colore preferito?")
    print("2 - Qual è il tuo animale preferito?")

    scelta = input("Scegli 1 o 2: ")

    # Struttura match-case 
    match scelta:
        case "1":
            risposta = input("Inserisci il tuo colore preferito: ")
            print("Hai impostato come risposta:", risposta)
        case "2":
            risposta = input("Inserisci il tuo animale preferito: ")
            print("Hai impostato come risposta:", risposta)
        case _:
            print(" Scelta non valida.")

    print("\n I tuoi dati sono stati aggiornati correttamente.")

# 3. Credenziali errate
else:
    print("\n Credenziali errate. Accesso negato.")
