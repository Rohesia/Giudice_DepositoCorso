from esercizio_riassuntivo1 import scegli_nota, scegli_durata

# Decoratore per separatore 
def separa(funzione):
    def wrapper(*args, **kwargs):
        print("\n==== Inizio sezione ====")
        risultato = funzione(*args, **kwargs)
        print("==== Fine sezione ====\n")
        return risultato
    return wrapper

# Funzione per creare melodia 
@separa
def crea_melodia(n):
    melodia = []
    for i in range(n):
        print(f"\n-- Nota {i+1} --")
        nota = scegli_nota()
        durata = scegli_durata()
        melodia.append((nota, durata))
    return melodia

# Stampa melodia
@separa
def stampa_melodia(melodia):
    print("Melodia completa:", melodia)
    print("\nNote separate:")
    for nota, durata in melodia:
        print(nota, end=" ")
    print()

# Analisi melodia
@separa
def analizza_melodia(melodia):
    for nota, durata in melodia:
        if durata >= 1:
            print(f"Nota lunga: {nota}")
        else:
            print(f"Nota breve: {nota}")

# Funzione ripetibile
def gioca():
    while True:
        n = int(input("\nQuante note vuoi generare? "))
        while n <= 0:
            print("Devi inserire un numero positivo!")
            n = int(input("Quante note vuoi generare? "))

        melodia = crea_melodia(n)
        stampa_melodia(melodia)
        analizza_melodia(melodia)

        ripeti = input("Vuoi creare un'altra melodia? (s/n): ")
        if ripeti.lower() != "s":
            print("Grazie per aver suonato! 🎵")
            break

# Avvio
gioca()
