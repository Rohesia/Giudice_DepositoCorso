# =======================================
# Classe base: Veicolo
# =======================================


class Veicolo:
    def __init__(self, marca:str, modello: str, anno: int, carburante: float = 100.0):
        self._marca = marca
        self._modello = modello
        self._anno = anno
        self._accensione = False # inizialmente è spento 
        self._carburante = carburante
        self._chilometri = 0
        
    def accendi(self) -> str:
        if self._accensione:
            return f"{self._marca} è accesa"
        if self._carburante <= 0:
            return f"{self.marca} non può accendersi perchè il carburante è esaurito"
        self._accensione = True 
        self._carburante -=1
        
    def spegni(self) -> str:
        if not self._accensione:
            return f"{self.marca} spenta"
        self._accensione = False 
        return f"{self._marca} accesa"
        
    def guida(self, km:float) -> str:
        if not self._accensione:
            return "accendi il veicolo"
        if self._carburante <= 0:
            self._accensione = False 
            return "carburante esaurito"
        self._chilometri += km
        self._carburante -= km * 0.1
        return f"Hai guidato {km} km. Carburante rimanente: {self._carburante:.1f}%"
        
    def __str__(self):
        stato = 'Acceso' if self.accensione else "Spento"
        return f"{self._marca} {self._modello} ({self._anno}) - {stato}"