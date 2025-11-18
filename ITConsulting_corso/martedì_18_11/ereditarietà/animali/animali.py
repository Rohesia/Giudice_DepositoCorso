# Classe base per tutti gli animali dello zoo
import random

class Animale:
    def __init__(self, nome: str, eta: int):
        self.nome = nome 
        self.eta = eta 
        
    def fai_suono(self):
        suoni_generici = ["Grrr!", "Mmmh!", "Brrr!"]
        suono = random.choice(suoni_generici)
        print(f"{self.nome} emette '{suono}")