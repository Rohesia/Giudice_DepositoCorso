# -----------------------------
# Classe base Persona
# -----------------------------

class Persona:
    def __init__(self, nome: str, eta: int):
        # Attributi privati con doppio underscore
        self.__nome = ""
        self.__eta = 0
        self.set_nome(nome)
        self.set_eta(eta)
        
    # Getter per il nome
    def get_nome(self) -> str:
        return self.__nome
    
    # Setter per il nome con validazione
    def set_nome(self, nome: str) -> None:
        nome_str = str(nome).strip()
        if nome_str:
            self.__nome = nome_str
    
    # Setter per l'età con validazione
    def set_eta(self, eta: int) -> None:
        eta_int = int(eta)
        if eta_int > 0:
            self.__eta = eta_int
        else:
            print("Valore non valido")
    
    # Metodo di presentazione
    def presentazione(self) -> str:
        return f"Mi chiamo {self.__nome} e ho {self.__eta} anni"