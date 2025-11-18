# Classe base per tutti i membri della squadra
class MembroSquadra:
    # ogni membro della squadra ha un nome ed una età
    def __init__(self, nome: str, eta: int):
        
        self.nome = nome
        self.eta = eta

    def descrivi(self):
        # descrizione con attributii per membro della squadra
        print(f"{self.nome}, {self.eta} anni, è un membro della squadra.")
