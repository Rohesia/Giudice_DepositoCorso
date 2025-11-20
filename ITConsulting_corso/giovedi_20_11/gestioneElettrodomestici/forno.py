# -------------------
# Sottoclasse forno
# -------------------
from elettrodomestico import Elettrodomestico

class Forno(Elettrodomestico):
    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str, tipo_alimentazione: str):
        super().__init__(marca, modello, anno_acquisto, guasto)
        # controllo tipo_alimentazione 
        if tipo_alimentazione != "elettrico" and tipo_alimentazione != "gas":
            print("Errore: tipo_alimentazione deve essere 'elettrico' o 'gas'")
            self.__tipo_alimentazione = "elettrico"  # valore di default
        else:
            self.__tipo_alimentazione = tipo_alimentazione

    # --- getter e setter (incapsulamento) ---
    def get_tipo_alimentazione(self) -> str:
        return self.__tipo_alimentazione

    def set_tipo_alimentazione(self, alimentazione):
        if alimentazione != "elettrico" and alimentazione != "gas":
            print("Errore: tipo_alimentazione deve essere 'elettrico' o 'gas'")
            return
        self.__tipo_alimentazione = alimentazione

    def stima_costo_base(self) -> float:
        """Forno: costo base dipende dal tipo di alimentazione."""
        base = 40.0
        if self.__tipo_alimentazione == "gas":
            base += 10.0  
        return base
