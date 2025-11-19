# -----------------------------
# Sottoclasse Studente
# ----------------------------- 
from persona import Persona


class Studente(Persona):
    def __init__(self, nome: str, eta: int):
        super().__init__(nome, eta)
        self.__voti = []  # lista interna dei voti
    
    # Metodo interno per aggiungere voto (non accessibile dall'esterno)
    def _aggiungi_voto(self, voto: int) -> None:
        if 0 <= voto <= 10:
            self.__voti.append(voto)
    
    # Metodo pubblico per calcolare la media
    def media(self) -> float:
        if not self.__voti:
            return 0.0
        return sum(self.__voti) / len(self.__voti)
    
    # Override presentazione
    def presentazione(self) -> str:
        return f"{super().presentazione()} La mia media dei voti è {self.media():.2f}."

    