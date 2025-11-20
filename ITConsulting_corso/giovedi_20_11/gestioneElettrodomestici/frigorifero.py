# -------------------
# Sottoclasse frigorifero
# ------------------- 
from elettrodomestico import Elettrodomestico

class Frigorifero(Elettrodomestico):
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, litri: int, ha_freezer: bool):
        super().__init__(marca, modello, anno_acquisto, guasto)
        # --- attributi privati ---
        self.__litri = int(litri)
        self.__ha_freezer = bool(ha_freezer)

    # --- getter e setter (incapsulamento) ---
    def get_litri(self) -> int:
        return self.__litri

    def set_litri(self, nuovo_litri):
        if type(nuovo_litri) != int:
            print("Errore: litri deve essere un intero")  
            return
        if nuovo_litri <= 0:
            print("Errore: litri deve essere positivo") 
            return
        self.__litri = nuovo_litri

    def get_ha_freezer(self) -> bool:
        return self.__ha_freezer

    def set_ha_freezer(self, nuovo_valore):
        if type(nuovo_valore) != bool:
            print("Errore: ha_freezer deve essere True o False")  
            return
        self.__ha_freezer = nuovo_valore

    def stima_costo_base(self) -> float:
        base = 45.0
        if self.__ha_freezer:
            base += 15.0
        if self.__litri > 300:
            base += 20.0
        return base
