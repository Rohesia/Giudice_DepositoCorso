from sottoclassi import *
from astrazione import VeicoloTrasporto

class GestoreFlotta:
    def __init__(self):
        self.veicoli = []   

    def aggiungi_veicolo(self, veicolo: VeicoloTrasporto):
        #Aggiunge un veicolo alla flotta
        if isinstance(veicolo, VeicoloTrasporto):
            self.veicoli.append(veicolo)
        else:
            raise TypeError("L'oggetto deve essere un VeicoloTrasporto.")

    def rimuovi_veicolo(self, targa: str):
        #Rimuove un veicolo dalla flotta tramite la targa
        for veicolo in self.veicoli:
            if veicolo._targa == targa:
                self.veicoli.remove(veicolo)
                return
        print("Veicolo non trovato.")

    def costo_totale_manutenzione(self) -> float:
        #Somma i costi di manutenzione di tutti i veicoli
        return sum(veicolo.costo_manutenzione() for veicolo in self.veicoli)

    def stampa_veicoli(self):
        #Elenca targa, tipo di veicolo e carico attuale
        if not self.veicoli:
            print("Nessun veicolo in flotta.")
            return

        for veicolo in self.veicoli:
            print(f"Targa: {veicolo._targa} | Tipo: {veicolo.__class__.__name__} | Carico attuale: {veicolo._carico_attuale} kg")
