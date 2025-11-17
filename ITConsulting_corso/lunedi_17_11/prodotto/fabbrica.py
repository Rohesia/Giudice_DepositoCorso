# ==========================================================
# CLASSE FABBRICA
# ==========================================================
from prodotto import * 

def separatore(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 40)
        risultato = func(*args, **kwargs)
        print("=" * 40 + "\n")
        return risultato
    return wrapper

class Fabbrica:
    def __init__(self, nome):
        self.nome = nome
        self.inventario = {}  
        self.prodotti = []    
        
    # aggiunta di prodotti    
    @separatore
    def aggiungi_prodotto(self, prodotto, quantita):
        if quantita <= 0:
            print("La quantità deve essere maggiore di zero.")
            return

        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
        else:
            self.inventario[prodotto] = quantita
            self.prodotti.append(prodotto)

        print(f"Aggiunti {quantita} unità di {prodotto.nome} all'inventario.")

# vendita di prodotti 
    @separatore
    def vendi_prodotto(self, prodotto, quantita):
        if prodotto not in self.inventario:
            print(f"{prodotto.nome} non presente in inventario.")
            return

        if quantita <= 0:
            print("La quantità deve essere maggiore di zero.")
            return

        if self.inventario[prodotto] >= quantita:
            self.inventario[prodotto] -= quantita
            profitto = prodotto.calcola_profitto() * quantita
            print(f"Venduti {quantita} di {prodotto.nome}. Profitto realizzato: {profitto}€")
            if self.inventario[prodotto] == 0:
                print(f"{prodotto.nome} esaurito in inventario!")
        else:
            print(f"Non ci sono abbastanza {prodotto.nome} in inventario per vendere {quantita} unità.")

# reso del prodotto
    @separatore
    def resi_prodotto(self, prodotto, quantita):
        if quantita <= 0:
            print("La quantità deve essere maggiore di zero.")
            return

        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
        else:
            self.inventario[prodotto] = quantita
            self.prodotti.append(prodotto)

        print(f"Resi {quantita} di {prodotto.nome}. Quantità attuale in inventario: {self.inventario[prodotto]}")

# mostra inventario 
    @separatore
    def mostra_inventario(self):
        print(f"Inventario fabbrica '{self.nome}':")
        if not self.inventario:
            print("Inventario vuoto")
        else:
            for prodotto, quantita in self.inventario.items():
                print(f"{prodotto} - Quantità: {quantita}")
