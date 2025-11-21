from abc import ABC, abstractmethod

class VeicoloTrasporto(ABC):
    def __init__(self, targa: str, peso_massimo: int):
        self._targa = targa
        self._peso_massimo = peso_massimo
        self._carico_attuale = 0

    # --- Metodo concreto ---
    def carica(self, peso: int):
        #Aggiunge peso al carico, se non supera la capacità
        if self._carico_attuale + peso <= self._peso_massimo:
            self._carico_attuale += peso
            print(f"Sono stati caricati {peso} kg. Carico attuale: {self._carico_attuale} kg.")
        else:
            print("Errore: il peso supera la capacità massima!")

    # --- Metodo concreto ---
    def scarica(self):
        #Svuota completamente il veicolo
        self._carico_attuale = 0
        print("Il veicolo è stato scaricato completamente.")

    # --- Metodo astratto ---
    @abstractmethod
    def costo_manutenzione(self) -> float:
        """Calcola il costo annuale di manutenzione."""
        pass
