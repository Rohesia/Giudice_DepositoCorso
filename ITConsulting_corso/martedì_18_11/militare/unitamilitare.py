# -----------------------------
# 1. Classe base: UnitaMilitare
# ----------------------------- 

class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome 
        self.numero_soldati = numero_soldati 
        
    # Metodo per far muovere l'unità
    def muovi(self):
        print(f"{self.nome} si sta muovendo")
        
    # Metodo per attaccare l'unità
    def attacca(self):
        print(f"{self.nome} sta attaccando il nemico!")
        

# Metodo per ritirare l'unità
    def ritira(self):
        print(f"{self.nome} sta effettuando una ritirata strategica.")