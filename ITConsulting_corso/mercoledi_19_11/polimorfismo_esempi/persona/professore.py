from persona import Persona  
from studente import Studente
# -----------------------------
# Sottoclasse Professore
# -----------------------------

class Professore(Persona):
    def __init__(self, nome: str, eta: int, materia: str):
        super().__init__(nome, eta)
        self.__materia = ""
        self.set_materia(materia)
    
    # Getter e setter materia
    def get_materia(self) -> str:
        return self.__materia
    
    def set_materia(self, materia: str) -> None:
        materia_str = str(materia).strip()
        if materia_str:
            self.__materia = materia_str
    
    # Metodo per assegnare voto a uno studente
    def assegna_voto(self, studente: Studente, voto: int) -> None:
        studente._aggiungi_voto(voto)
    
    # Override presentazione
    def presentazione(self) -> str:
        return f"{super().presentazione()} Insegno la materia: {self.__materia}."
