# -------------------
# Sottoclasse Lavatrice
# -------------------
from elettrodomestico import Elettrodomestico

class Lavatrice(Elettrodomestico):
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, kg: int, giri_centrifuga: int):
        super().__init__(marca, modello, anno_acquisto, guasto)
        # --- attributi privati ---
        self.__kg = int(kg)
        self.__giri_centrifuga = int(giri_centrifuga)

    # --- getter e setter (incapsulamento) ---
    def get_kg(self) -> int:
        return self.__kg

    def set_kg(self, nuovo_valore: int):
        if not isinstance(nuovo_valore, int):
            print("Errore: kg deve essere un intero")  
            return
        if nuovo_valore <= 0:
            print("Errore: kg deve essere positivo")  
            return
        self.__kg = nuovo_valore

    def get_giri_centrifuga(self) -> int:
        return self.__giri_centrifuga

    def set_giri_centrifuga(self, nuovo_valore: int):
        if not isinstance(nuovo_valore, int):
            print("Errore: giri centrifuga deve essere un intero") 
            return
        if nuovo_valore <= 0:
            print("Errore: giri centrifuga deve essere positivo") 
            return
        self.__giri_centrifuga = nuovo_valore

    def stima_costo_base(self) -> float:
        # Lavatrice: costo base più alto per complessità meccanica
        base = 50.0
        # leggera aumento se kg grande o giri molto alti
        if self.__kg >= 10:
            base += 10.0
        if self.__giri_centrifuga >= 1400:
            base += 5.0
        return base
