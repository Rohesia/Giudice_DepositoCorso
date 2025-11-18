# -------------------------------------------------
# 3. Classe ControlloMilitare (gestione delle unità)
# ------------------------------------------------- 
from classiderivate import *

# -----------------------------
# 3. Classe ControlloMilitare
# -----------------------------
class ControlloMilitare:
    # Costruttore: inizializza un dizionario vuoto per registrare le unità
    def __init__(self):
        self.unita_registrate = {}

    # Metodo per registrare un'unità nel sistema
    def registra_unita(self, unita):
        self.unita_registrate[unita.nome] = unita
        print(f"Unità '{unita.nome}' registrata con successo.")

    # Metodo per mostrare tutte le unità registrate
    def mostra_unita(self):
        if not self.unita_registrate:
            print("Nessuna unità registrata.")
            return
        print("Unità registrate:")
        for nome in self.unita_registrate:
            print(f" - {nome}")

    # Metodo per mostrare i dettagli di una singola unità
    def dettagli_unita(self, nome):
        if nome not in self.unita_registrate:
            print(f"Unità '{nome}' non trovata.")
            return
        u = self.unita_registrate[nome]
        print(f"Dettagli dell'unità '{nome}':")
        print(f" • Numero soldati: {u.numero_soldati}")
        # Mostriamo anche lo stato interno specifico di ogni tipo di unità
        if isinstance(u, Fanteria):
            print(f" • Trincee costruite: {u.trincee_costruite}")
        elif isinstance(u, Artiglieria):
            print(f" • Bersagli calibrati: {u.bersagli_calibrati}")
        elif isinstance(u, Cavalleria):
            print(f" • Terreni esplorati: {len(u.terreni_esplorati)}")
        elif isinstance(u, SupportoLogistico):
            print(f" • Rifornimenti effettuati: {u.rifornimenti_effettuati}")
        elif isinstance(u, Ricognizione):
            print(f" • Missioni completate: {u.missioni_completate}")