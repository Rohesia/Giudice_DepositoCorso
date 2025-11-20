# ----------------------------
# Classi Impiegati
# ----------------------------
from abc import ABC, abstractmethod 

class Impiegato(ABC):
    def __init__(self, nome: str, cognome: str, stipendio_base: float):
        self.nome = nome
        self.cognome = cognome
        self.stipendio_base = stipendio_base

    @abstractmethod
    def calcola_stipendio(self) -> float:
        pass

    def __str__(self):
        return f"{self.nome} {self.cognome}"

class Fisso(Impiegato):
    def calcola_stipendio(self) -> float:
        return self.stipendio_base

class Provvigione(Impiegato):
    def __init__(self, nome: str, cognome: str, stipendio_base: float, vendite: float, percentuale_bonus: float):
        super().__init__(nome, cognome, stipendio_base)
        self.vendite = vendite
        self.percentuale_bonus = percentuale_bonus

    def calcola_stipendio(self) -> float:
        return self.stipendio_base + self.vendite * self.percentuale_bonus
    
    
# matrioska 
class ConRimborso(Impiegato, ABC):
    def __init__(self, nome: str, cognome: str, stipendio_base: float, rimborso: float):
        super().__init__(nome, cognome, stipendio_base)
        self.rimborso = rimborso

    @abstractmethod
    def calcola_stipendio(self) -> float:
        pass

class ImpiegatoRimborsoMensile(ConRimborso):
    def calcola_stipendio(self) -> float:
        return self.stipendio_base + self.rimborso
