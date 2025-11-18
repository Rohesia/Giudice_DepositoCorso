# -----------------------------
# 2. Classi Derivate
# -----------------------------

from unitamilitare import UnitaMilitare

# Fanteria con azione speciale "costruire trincee"
class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        self.trincee_costruite = 0   #  trincee costruite

    def costruisci_trincea(self):
        self.trincee_costruite += 1
        print(f"{self.nome}: ha costruito una trincea (totale: {self.trincee_costruite})")

    # Metodo uniforme per eseguire l'azione speciale
    def azione_speciale(self):
        self.costruisci_trincea()

# Artiglieria con azione speciale "calibrare artiglieria"
class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        self.bersagli_calibrati = 0   # numero bersagli calibrati

    def calibra_artiglieria(self):
        self.bersagli_calibrati += 1
        print(f"{self.nome}: calibrazione completata (bersagli calibrati: {self.bersagli_calibrati})")

    def azione_speciale(self):
        self.calibra_artiglieria()

# Cavalleria con azione speciale "esplorare terreno"
class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        self.terreni_esplorati = []   # lista terreni esplorati

    def esplora_terreno(self, nome_terreno="territorio sconosciuto"):
        self.terreni_esplorati.append(nome_terreno)
        print(f"{self.nome}: esplorato {nome_terreno} (totale esplorazioni: {len(self.terreni_esplorati)})")

    def azione_speciale(self):
        self.esplora_terreno("collina vicina")

# Supporto logistico con azione speciale "rifornire unità"
class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        self.rifornimenti_effettuati = 0  # contatore rifornimenti

    def rifornisci_unita(self):
        self.rifornimenti_effettuati += 1
        print(f"{self.nome}: rifornimento completato (totale rifornimenti: {self.rifornimenti_effettuati})")

    def azione_speciale(self):
        self.rifornisci_unita()

# Ricognizione con azione speciale "condurre ricognizione"
class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super().__init__(nome, numero_soldati)
        self.missioni_completate = 0   # numero missioni completate

    def conduci_ricognizione(self):
        self.missioni_completate += 1
        print(f"{self.nome}: missione completata (totale missioni: {self.missioni_completate})")

    def azione_speciale(self):
        self.conduci_ricognizione()

