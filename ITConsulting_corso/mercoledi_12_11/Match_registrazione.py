# ==========================================================
# REGISTRAZIONE e LOGIN
# ==========================================================

print("==========================================================")
print(" BENVENUTO! Se non hai un account, registrati prima.")
print("==========================================================")

# 1. registrazione
nuovo_nome = input("Crea il tuo nome utente: ")
nuova_password = input("Crea la tua password: ")

print("\n Registrazione completata con successo!")
print("Ora effettua il login con le tue credenziali.\n")

# 2. login
nome = input("Inserisci nome utente: ")
password = input("Inserisci password: ")

# Verifica delle credenziali
if nome == nuovo_nome and password == nuova_password:
    print("\n Accesso riuscito! Benvenuto", nome)

    # modificare la password
    modifica = input("Vuoi cambiare la tua password? (s/n): ")
    if modifica.lower() == "s":
        nuova_password = input("Inserisci la nuova password: ")
        print(" Password aggiornata con successo!")
    else:
        print("La password resta invariata.")

    # 3. Domande segrete
    print("\nScegli una domanda segreta:")
    print("1 - Qual è il tuo colore preferito?")
    print("2 - Qual è il tuo animale preferito?")

    scelta = input("Scegli 1 o 2: ")

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

else:
    # Se le credenziali non corrispondono
    print("\n Credenziali errate. Accesso negato.")
