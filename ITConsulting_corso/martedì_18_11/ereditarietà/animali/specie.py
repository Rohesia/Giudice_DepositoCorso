from animali import Animale 
import random
# import la classe base Animale dal file animali.p

# ------------------------------------------------
# Classe Leone: rappresenta un leone nello zoo
# ------------------------------------------------

class Leone(Animale):
    def __init__(self, nome:str, eta: int, velocita: float):
        super().__init__(nome, eta) #  costruttore della classe base
        self.velocita = velocita
        
    def fai_suono(self):
        suoni = ["Rooooar!", "Grrrrr!", "Raaah!"]
        print(f"{self.nome} ruggisce: {random.choice(suoni)}")
        
    def caccia(self):
        print(f"{self.nome} sta cacciando con la sefuente forza {self.velocita}")
        
        
# ------------------------------------------------
# Classe Giraffa
# ------------------------------------------------
class Giraffa(Animale):
    def __init__(self, nome: str, eta: int, attenzione: int):
        super().__init__(nome, eta)
        self.attenzione = attenzione 

    def fai_suono(self):
        suoni = ["Mmmh!", "Humm!", "Ehh!"]
        print(f"{self.nome} emette un suono: {random.choice(suoni)}")

    def osserva(self):
        print(f"{self.nome} sta osservando l'ambiente con attenzione: {self.attenzione}/10")

# ------------------------------------------------
# Classe Pinguino
# ------------------------------------------------ 
class Pinguino(Animale):
    def __init__(self, nome: str, eta: int, cammino: float):
        super().__init__(nome, eta)
        self. cammino =  cammino  

    def fai_suono(self):
        suoni = ["Piii!", "Graaah!", "Chirp!"]
        print(f"{self.nome} gracchia: {random.choice(suoni)}")

    def cammina(self):
        print(f"{self.nome} cammina a {self.cammino} m/s!")

# ------------------------------------------------
# Classe Elefante
# ------------------------------------------------
class Elefante(Animale):
    pass  

