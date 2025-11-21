from astrazione import VeicoloTrasporto


# sottoclasse Camion
class Camion(VeicoloTrasporto):
    def __init__(self, targa: str, peso_massimo: int, numero_assi: int):
        super().__init__(targa, peso_massimo)
        self._numero_assi = numero_assi

    def costo_manutenzione(self) -> float:
        return 100 * self._numero_assi + 1 * self._peso_massimo


# sottoclasse Furgone
class Furgone(VeicoloTrasporto):
    def __init__(self, targa: str, peso_massimo: int, alimentazione: str):
        super().__init__(targa, peso_massimo)
        self._alimentazione = alimentazione.lower()

    def costo_manutenzione(self) -> float:
        if self._alimentazione == "elettrico":
            return 200
        elif self._alimentazione == "diesel":
            return 150
        else:
            print("Alimentazione non valida. Usa 'elettrico' o 'diesel'.")


# sottoclasse Motocarro 
class Motocarro(VeicoloTrasporto):
    def __init__(self, targa: str, peso_massimo: int, anni_servizio: int):
        super().__init__(targa, peso_massimo)
        self._anni_servizio = anni_servizio

    def costo_manutenzione(self) -> float:
        return 50 * self._anni_servizio
