# ==========================================================
# CLASSE Automobile
# ==========================================================
'''
class Automobile: 
    numero_di_ruote = 4
    def __init__(self, marca, modello):
        self.marca = marca 
        self.modello = modello 
    def stampa_info(self):
        print("L'automobile è una", self.marca, self.modello)
        
auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")

auto1.stampa_info()
auto2.stampa_info()

def __str__(self):
    return f"Persona(nome={self.nome}, eta = {self.eta})"
'''
# ==========================================================
# CLASSE Calcolatrice
# ==========================================================

class Calcolatrice:
    @staticmethod
    def somma(a, b):
        return a + b 

# uso del metodo statico 
risultato = Calcolatrice.somma(5, 3)

print(risultato)

# ==========================================================
# CLASSE Contatore
# ==========================================================

class Contatore:
    numero_istanze = 0 # attributo di classe 
    
    def __init__(self):
        Contatore.numero_istanze += 1
    
    @classmethod
    def mostra_numero_istanze(cls):
        print(f"sono state create {cls.numero_istanze} istanze")
        
# creazione di istanze 
c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()
# output: sono state create 2 istanze
