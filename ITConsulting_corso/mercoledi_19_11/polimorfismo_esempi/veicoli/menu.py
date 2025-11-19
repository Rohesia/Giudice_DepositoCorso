from auto import * 
from gestoreveicoli import GestoreParcoVeicoli
from veicoli import *

def leggi_float(messaggio: str) -> float:
    while True:
        valore = input(messaggio).strip().replace(",", ".")
        if valore == float(valore):
            return valore
        else:
            print("Valore non valido. Inserisci un numero valido.")
        
        
# menu 
def menu():
    gestore = GestoreParcoVeicoli()

    while True:
        print("\n=== MENU PARCO VEICOLI ===")
        print("1. Aggiungi veicolo")
        print("2. Rimuovi veicolo")
        print("3. Lista veicoli")
        print("4. Accendi veicolo")
        print("5. Spegni veicolo")
        print("6. Guida veicolo")
        print("7. Suona clacson (Auto)")
        print("8. Carica/Scarica Furgone")
        print("9. Esegui Wheelie (Moto)")
        print("10. Esci")

        scelta = input("Scegli un'opzione: ").strip()

        if scelta == "1":
            tipo = input("Tipo veicolo (Auto/Furgone/Moto): ").strip().lower()
            marca = input("Marca: ").strip()
            modello = input("Modello: ").strip()
            anno = int(input("Anno: ").strip())

            if tipo == "auto":
                porte = int(input("Numero di porte: "))
                veicolo = Auto(marca, modello, anno, porte)
            elif tipo == "furgone":
                capacita = float(input("Capacità carico (kg): "))
                veicolo = Furgone(marca, modello, anno, capacita)
            elif tipo == "moto":
                tipo_moto = input("Tipo moto (sportiva/touring): ").strip()
                veicolo = Motocicletta(marca, modello, anno, tipo_moto)
            else:
                print("Tipo veicolo non valido.")
                continue

            gestore.aggiungi_veicolo(veicolo)
            print(f"{tipo.capitalize()} aggiunta al parco.")

        elif scelta == "2":
            marca = input("Marca del veicolo da rimuovere: ").strip()
            modello = input("Modello del veicolo da rimuovere: ").strip()
            if gestore.rimuovi_veicolo(marca, modello):
                print("Veicolo rimosso.")
            else:
                print("Veicolo non trovato.")

        elif scelta == "3":
            veicoli = gestore.lista_veicoli()
            if veicoli:
                for v in veicoli:
                    print(v)

        elif scelta == "4":
            marca = input("Marca veicolo da accendere: ").strip()
            modello = input("Modello veicolo da accendere: ").strip()
            v = gestore.trova_veicolo(marca, modello)
            if v:
                print(v.accendi())
            else:
                print("Veicolo non trovato.")

        elif scelta == "5":
            marca = input("Marca veicolo da spegnere: ").strip()
            modello = input("Modello veicolo da spegnere: ").strip()
            v = gestore.trova_veicolo(marca, modello)
            if v:
                print(v.spegni())
            else:
                print("Veicolo non trovato.")

        elif scelta == "6":
            marca = input("Marca veicolo da guidare: ").strip()
            modello = input("Modello veicolo da guidare: ").strip()
            v = gestore.trova_veicolo(marca, modello)
            if v:
                km = leggi_float("Quanti km vuoi percorrere? ")
                print(v.guida(km))
            else:
                print("Veicolo non trovato.")

        elif scelta == "7":
            marca = input("Marca Auto: ").strip()
            modello = input("Modello Auto: ").strip()
            v = gestore.trova_veicolo(marca, modello)
            if isinstance(v, Auto):
                print(v.suona_clacson())
            else:
                print("Veicolo non trovato o non è un'Auto.")

        elif scelta == "8":
            marca = input("Marca Furgone: ").strip()
            modello = input("Modello Furgone: ").strip()
            v = gestore.trova_veicolo(marca, modello)
            if isinstance(v, Furgone):
                azione = input("Vuoi caricare o scaricare? (C/S): ").strip().upper()
                peso = leggi_float("Inserisci peso (kg): ")
                if azione == "C":
                    print(v.carica(peso))
                elif azione == "S":
                    print(v.scarica(peso))
            else:
                print("Veicolo non trovato o non è un Furgone.")

        elif scelta == "9":
            marca = input("Marca Moto: ").strip()
            modello = input("Modello Moto: ").strip()
            v = gestore.trova_veicolo(marca, modello)
            if isinstance(v, Motocicletta):
                print(v.esegui_wheelie())
            else:
                print("Veicolo non trovato o non è una Moto.")

        elif scelta == "10":
            print("Uscita dal programma.")
            break

        else:
            print("Opzione non valida.")
            

menu()