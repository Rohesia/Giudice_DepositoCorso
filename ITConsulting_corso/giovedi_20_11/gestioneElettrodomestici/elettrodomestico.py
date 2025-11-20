import datetime

class Elettrodomestico:
    def __init__(self, marca: str, modello: str, anno_acq: int, guasto: str):
        # --- INCAPSULAMENTO ---
        self.__marca = marca
        self.__modello = modello
        self.__anno_acq = anno_acq
        self.__guasto = guasto

    # --- getter e setter ---
    # metodo get per leggere l'attributo privato
    # metodo set per modificarlo in modo controllato

    # ---- MARCA ----
    def get_marca(self) -> str:
        return self.__marca
    
    def set_marca(self, nuovo_valore: str):
        if not isinstance(nuovo_valore, str):
            print("Errore: marca deve essere una stringa")  
            return
        self.__marca = nuovo_valore

    # ---- MODELLO ----
    def get_modello(self) -> str:
        return self.__modello
    
    def set_modello(self, nuovo_valore: str):
        if not isinstance(nuovo_valore, str):
            print("Errore: modello deve essere una stringa") 
            return
        self.__modello = nuovo_valore

    # ---- ANNO ACQUISTO ----
    def get_anno_acquisto(self) -> int:
        return self.__anno_acq
    
    def set_anno_acquisto(self, nuovo_valore: int):
        if not isinstance(nuovo_valore, int):
            print("Errore: anno deve essere un intero") 
            return
        current_year = datetime.date.today().year
        if nuovo_valore > current_year:
            print("Errore: anno di acquisto non può essere nel futuro")  
            return
        self.__anno_acq = nuovo_valore

    # ---- GUASTO ----
    def get_guasto(self) -> str:
        return self.__guasto
    
    def set_guasto(self, nuovo_valore: str):
        if not isinstance(nuovo_valore, str):
            print("Errore: guasto deve essere una stringa")  
            return
        self.__guasto = nuovo_valore
        
    # --- altri metodi ---
    def descrizione(self) -> str:
        return (f"{self.get_marca()} {self.get_modello()} "
                f"({self.get_anno_acquisto()}) - Guasto: {self.get_guasto()}")

    def stima_costo_base(self) -> float:
        return 30.0

    def __repr__(self):
        return f"<Elettrodomestico: {self.get_marca()} {self.get_modello()}>"
