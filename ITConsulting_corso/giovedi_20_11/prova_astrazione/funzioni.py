# ----------------------------
# Funzioni menu
# ----------------------------
from esercizio import *

impiegati = []

def aggiungi_fisso():
    nome = input("Nome: ").strip()
    cognome = input("Cognome: ").strip()
    stipendio_base = float(input("Stipendio base: "))
    imp = Fisso(nome, cognome, stipendio_base)
    impiegati.append(imp)
    print(f"Aggiunto impiegato fisso: {imp}")

def aggiungi_provvigione():
    nome = input("Nome: ").strip()
    cognome = input("Cognome: ").strip()
    stipendio_base = float(input("Stipendio base: "))
    vendite = float(input("Totale vendite: "))
    percentuale_bonus = float(input("Percentuale bonus (es. 5 per 5%): ")) / 100
    imp = Provvigione(nome, cognome, stipendio_base, vendite, percentuale_bonus)
    impiegati.append(imp)
    print(f"Aggiunto impiegato a provvigione: {imp}")

def mostra_impiegati():
    if not impiegati:
        print("Nessun impiegato presente.")
        return
    print("\n--- Lista Impiegati ---")
    for imp in impiegati:
        print(f"{imp} -> Stipendio: {imp.calcola_stipendio():.2f} €")
        
def aggiungi_rimborso():
    nome = input("Nome: ").strip()
    cognome = input("Cognome: ").strip()
    stipendio_base = float(input("Stipendio base: "))
    rimborso = float(input("Rimborso mensile: "))
    imp = ImpiegatoRimborsoMensile(nome, cognome, stipendio_base, rimborso)
    impiegati.append(imp)
    print(f"Aggiunto impiegato con rimborso: {imp}")
