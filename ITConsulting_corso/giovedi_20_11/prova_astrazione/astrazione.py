# esempio 1
from abc import ABC, abstractmethod

class Animale(ABC):
    @abstractmethod 
    def muovi(self):
        pass 
    
class Cane(Animale):
    def muovi(self):
        print("Corro")
        
class Pesce(Animale):
    def muovi(self):
        print("Nuoto")
        
# Prova delle classi concrete
c = Cane()
p = Pesce()

c.muovi()  # Output: Corro
p.muovi()  # Output: Nuoto


# esempio 2 
from abc import ABC, abstractmethod

# Classe astratta Forma
class Forma(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass

# Classe concreta Rettangolo
class Rettangolo(Forma):
    def __init__(self, larghezza, altezza):
        self.larghezza = larghezza
        self.altezza = altezza
    
    def area(self):
        return self.larghezza * self.altezza
    
    def perimetro(self):
        return 2 * (self.larghezza + self.altezza)

# Tentativo di istanziare classe astratta (genera errore)
# f = Forma()  # TypeError: Can't instantiate abstract class Forma

# Uso corretto: istanziare la classe concreta
r = Rettangolo(5, 10)
print(r.area())       # Output: 50
print(r.perimetro())  # Output: 30





        
        
