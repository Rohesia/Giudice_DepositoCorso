from professore import Professore
from studente import Studente
# -----------------------------
# Funzioni di input
# -----------------------------
def leggi_eta(messaggio: str) -> int:
    while True:
        valore = input(messaggio).strip()
        if valore.isdigit():
            eta = int(valore)
            if eta > 0:
                return eta
        print("Valore non valido. Inserisci un numero intero positivo.")

def leggi_voto(messaggio: str) -> int:
    while True:
        valore = input(messaggio).strip()
        if valore.isdigit():
            voto = int(valore)
            if 0 <= voto <= 10:
                return voto
        print("Valore non valido. Inserisci un numero da 0 a 10.")

# -----------------------------
# Menu principale
# -----------------------------
def menu():
    studenti: list[Studente] = []
    professori: list[Professore] = []

    while True:
        print("\n=== Menu Gestione Scuola ===")
        print("1. Aggiungi Studente")
        print("2. Aggiungi Professore e assegna voti")
        print("3. Mostra tutti gli Studenti")
        print("4. Mostra tutti i Professori")
        print("5. Esci")
        scelta = input("Scegli un'opzione (1-5): ").strip()

        if scelta == "1":
            nome = input("Nome studente: ").strip()
            eta = leggi_eta("Età studente: ")
            studente = Studente(nome, eta)
            studenti.append(studente)
            print(f"Studente {nome} aggiunto.")

        elif scelta == "2":
            nome = input("Nome professore: ").strip()
            eta = leggi_eta("Età professore: ")
            materia = input("Materia insegnata: ").strip()
            professore = Professore(nome, eta, materia)
            professori.append(professore)
            print(f"Professore {nome} aggiunto.")

            # Assegna voti agli studenti registrati
            if not studenti:
                print("Non ci sono studenti a cui assegnare voti.")
            else:
                print("Assegna voti agli studenti registrati:")
                for studente in studenti:
                    voto = leggi_voto(f"Inserisci il voto per {studente.get_nome()}: ")
                    professore.assegna_voto(studente, voto)
                    print(f"Voto {voto} assegnato a {studente.get_nome()} da {professore.get_nome()}.")

        elif scelta == "3":
            print("\n=== Studenti ===")
            for s in studenti:
                print(s.presentazione())

        elif scelta == "4":
            print("\n=== Professori ===")
            for p in professori:
                print(p.presentazione())

        elif scelta == "5":
            print("Uscita dal programma. Arrivederci!")
            break

        else:
            print("Opzione non valida. Riprova.")

# Avvio del menu
menu()