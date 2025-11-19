from incapsulamento import *

def leggi_saldo(prompt: str) -> float:
    while True:
        valore = input(prompt).strip().replace(",", ".")
        if valore.count(".") <= 1 and all(c in "0123456789." for c in valore):
            numero = float(valore)
            if numero >= 0:
                return numero
        print("Valore non valido. Reinserisci un numero positivo.")

def menu():
    print("==== Creazione del conto ======")
    nome = input("Inserisci il titolare: ").strip()
    while not nome:
        nome = input("Il nome insrito non è valido: ").strip()

    saldo_iniziale = leggi_saldo("Inserisci il saldo iniziale se non è presente inserisci 0: ")

    conto = ContoBancario(nome, saldo_iniziale)

    while True:
        print("\n=== Menu Conto Bancario ===")
        print("1. Visualizza saldo")
        print("2. Deposita denaro")
        print("3. Preleva denaro")
        print("4. Esci")
        scelta = input("Scegli un'opzione (1-4): ").strip()

        if scelta == "1":
            print(f"Saldo attuale: {conto.visualizza_saldo():.2f} €")
        elif scelta == "2":
            importo = leggi_saldo("Inserisci importo da depositare: ")
            conto.deposita(importo)
            print(f"Deposito effettuato. Nuovo saldo: {conto.visualizza_saldo():.2f} €")
        elif scelta == "3":
            importo = leggi_saldo("Inserisci importo da prelevare: ")
            if importo <= conto.visualizza_saldo():
                conto.preleva(importo)
                print(f"Prelievo effettuato. Nuovo saldo: {conto.visualizza_saldo():.2f} €")
            else:
                print("Saldo insufficiente per il prelievo.")
        elif scelta == "4":
            print("Uscita dal programma. Arrivederci!")
            break
        else:
            print("Opzione non valida. Riprova.")

menu()
