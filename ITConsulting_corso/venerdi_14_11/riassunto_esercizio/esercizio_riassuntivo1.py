# ==========================================================
# Generatore di note musicali 
# ==========================================================

# Decoratore 
def suona(funzione):
    def wrapper(*args, **kwargs):
        print("\n🎵 Inizio a suonare la funzione...")
        risultato = funzione(*args, **kwargs)
        print("🎶 Funzione terminata!\n")
        return risultato
    return wrapper

# Liste note 
note = ["C", "D", "E", "F", "G", "A", "B"]

# durate
durate = [1, 0.5, 0.25]

# Funzioni decorate
@suona
def scegli_nota():
    print("Scegli una nota tra:", note)
    scelta = input("Inserisci la nota: ")
    while scelta not in note:
        print("Nota non valida. Riprova!")
        scelta = input("Inserisci la nota: ")
    return scelta

@suona
def scegli_durata():
    print("Scegli una durata tra:", durate)
    scelta = input("Inserisci la durata: ")
    while scelta not in ["1", "0.5", "0.25"]:
        print("Durata non valida. Riprova!")
        scelta = input("Inserisci la durata: ")
    return float(scelta)
