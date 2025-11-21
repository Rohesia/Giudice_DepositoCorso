from abc import ABC, abstractmethod
from badge import Badge
from turno import Turno
from log import LogIngresso

# =========================================
# ASTRAZIONE: Classe base astratta per tutte le persone
# =========================================
class Persona(ABC):
    #Classe astratta che rappresenta una persona in azienda

    def __init__(self, nome: str, cognome: str, cf: str):
        self.__nome = nome
        self.__cognome = cognome
        self.__cf = cf

    # GETTER
    def get_nome_completo(self) -> str:
        return f"{self.__nome} {self.__cognome} ({self.__cf})"

    @abstractmethod
    def info(self) -> str:
        pass

    # =========================================
    # ASTRAZIONE dentro ASTRAZIONE
    # =========================================
    class Accesso(ABC):
        @abstractmethod
        def entra_in_azienda(self, ora_corrente: str, log: LogIngresso):
            pass

        @abstractmethod
        def esce_dall_azienda(self, ora_corrente: str, log: LogIngresso):
            pass
