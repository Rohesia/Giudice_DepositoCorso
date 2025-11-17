# ==========================================================
# DIZIONARI
# ==========================================================
""" 
studente = {
    "nome": "Alice",
    "età": 20, 
    "sesso": "Femmina"
}

print(studente["nome"])
print(studente["età"])

studente["città"] = "Roma"
print(studente)

print(studente.keys())
print(studente.values())
print(studente.items())
print(studente.get("nome")) """

# ==========================================================
# CREAZIONE DIZIONARIO 
# ==========================================================

# ==========================================================
# CREAZIONE DIZIONARIO PIANTA
# ==========================================================

# dizionario vuoto
pianta = {}

# inserimento dati tramite input
pianta["nome"] = input("Inserisci il nome della pianta: ")
pianta["specie"] = input("Inserisci la specie della pianta: ")
pianta["altezza"] = float(input("Inserisci l'altezza della pianta (in cm): "))
pianta["sempreverde"] = input("la pianta è sempreverde? inserisci solo True o False").lower()

# stampa chiave-valore
print("\nDati della pianta:")
for chiave, valore in pianta.items():
    print(f"{chiave} -> {valore}")

# stampa singola 
# chiave
print("Chiavi:")
for chiave in pianta.keys():
    print(chiave)

# valori
print("\nValori:")
for valore in pianta.values():
    print(valore)
