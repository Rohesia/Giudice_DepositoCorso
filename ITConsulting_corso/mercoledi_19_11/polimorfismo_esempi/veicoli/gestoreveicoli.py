# =======================================
# Classe Gestore del Parco Veicoli
# =======================================
from veicoli import Veicolo
from auto import *

class GestoreParcoVeicoli:
    def __init__(self):
        self._veicoli = []

    def aggiungi_veicolo(self, veicolo: Veicolo):
        self._veicoli.append(veicolo)

    def rimuovi_veicolo(self, marca: str, modello: str):
        for v in self._veicoli:
            if v._marca == marca and v._modello == modello:
                self._veicoli.remove(v)
                return True
        return False

    def lista_veicoli(self):
        if not self._veicoli:
            print("Nessun veicolo nel parco.")
        else:
            print("\n=== PARCO VEICOLI ===")
            for v in self._veicoli:
                print(v)
                
    def trova_veicolo(self, marca: str, modello: str):
        for v in self._veicoli:
            if v._marca == marca and v._modello == modello:
                return v
        return None

    def conta_veicoli(self) -> int:
        return len(self._veicoli)