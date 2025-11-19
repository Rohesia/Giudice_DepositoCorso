from veicoli import Veicolo

# =======================================
# Classe derivata: Auto
# =======================================

class Auto(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, numero_porte: int, carburante: float = 100.0):
        super().__init__(marca, modello, anno, carburante)
        self._numero_porte = numero_porte

    def suona_clacson(self) -> str:
        if self._accensione == True:
            return "Beep! Beep!"

    def __str__(self):
        return f"AUTO → {super().__str__()} - Porte: {self._numero_porte}"


# =======================================
# Classe derivata: Furgone
# =======================================

class Furgone(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, capacita_carico: float, carburante: float = 100.0):
        super().__init__(marca, modello, anno, carburante)
        self._capacita_carico = capacita_carico  

    def carica(self, peso: float) -> str:
        if self._caricato + peso > self._capacita_carico:
            return "Il furgone sta caricando la merce."
        self._caricato += peso
        return f"sono stati caricati {peso} kg. il totale è di: {self._caricato}"

    def scarica(self, peso: float) -> str:
        if peso > self._caricato:
            peso = self._caricato
        self._caricato -= peso
        return f"sono stati scaricati {peso} kg. totale: {self._caricato}kg"

    def __str__(self):
        return f"FURGONE → {super().__str__()} - Capacità carico: {self._capacita_carico} kg"


# =======================================
# Classe derivata: Motocicletta
# =======================================

class Motocicletta(Veicolo):
    def __init__(self, marca: str, modello: str, anno: int, tipo: str, carburante: float = 100.0):
        super().__init__(marca, modello, anno, carburante)
        self._tipo = tipo.lower()

    def esegui_wheelie(self) -> str:
        if not self._accensione:
            return "accendi la moto prima di fare un wheelie"
        if self._tipo == "sportiva":
            return "La moto fa un wheelie!"
        return "Questa moto non è adatta ai wheelie."
    
    def rifornisci(self, litri: float) -> None:
        if litri > 0:
            self._carburante = min(self._carburante + litri, 100.0)

    def __str__(self) -> str:
        stato = "Accesa" if self._accensione else "Spenta"
        return f"MOTO → {self._marca} {self._modello} ({self._anno}) - Tipo: {self._tipo} - Stato: {stato} - Carburante: {self._carburante:.0f}%"