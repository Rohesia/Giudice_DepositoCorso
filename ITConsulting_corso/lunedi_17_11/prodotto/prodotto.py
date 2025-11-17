# ==========================================================
# CLASSE BASE PRODOTTO
# ==========================================================

class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome 
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione
    
    def __str__(self):
        return f"Nome del Prodotto {self.nome} (ha un costo di produzione di: {self.costo_produzione}€, ed un prezzo di: {self.prezzo_vendita}€)"

# ==========================================================
# CLASSI PARALLELE
# ==========================================================

# classe Elettronica 
class Elettronica:
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.garanzia = garanzia

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

    def __str__(self):
        return f"Nome del Prodotto {self.nome} (costo: {self.costo_produzione}€, prezzo: {self.prezzo_vendita}€, garanzia: {self.garanzia} anni)"

        
# classe Abbigliamento
class Abbigliamento:
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.materiale = materiale

    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

    def __str__(self):
        return f"Nome del Prodotto {self.nome} (costo: {self.costo_produzione}€, prezzo: {self.prezzo_vendita}€, materiale: {self.materiale})"
