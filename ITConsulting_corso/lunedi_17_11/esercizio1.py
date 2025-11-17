# ==========================================================
# CLASSE PUNTO
# ==========================================================

import math 

# classe punto 
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    # spostare il punto di dx e dy 
    def spostamento(self, dx, dy):
        self.x += dx 
        self.y += dy 
        
    # calcolo della distanza dall'origine 
    def distanza(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    # stampa del punto con metodo speciale __str__
    def __str__(self):
        return f"Coordinate spaziali x = {self.x}, y = {self.y}"
    

# oggetti della classe 
punto1 = Punto(3, 4)
punto2 = Punto(0, 0)

lista_punti = [punto1, punto2]

# stampa di tutti i punti usando __str__
print("stampa i punti della lista: ")
for punto in lista_punti:
    print(punto)
    
#stampa 
print(punto1)
print(punto2)

punto1.spostamento(7, 9)
print("\nDopo lo spostamento di punto1:")
for punto in lista_punti:
    print(punto)

# distanza di tutti i punti dall'origine
print("\nDistanza dei punti dall'origine:")
for punto in lista_punti:
    print(f"{punto} → distanza: {punto.distanza()}")