# ==========================================================
# MODULO PER ANALISI VENDITE
# ==========================================================

class AnalisiVendite:
    #Classe per i dati di vendita

    def __init__(self, vendite):
        # lista di numeri interi
        self.vendite = vendite

    def totale(self):
        # totale delle vendite
        return sum(self.vendite)

    def media(self):
        # media delle vendite
        if len(self.vendite) == 0:
            return 0
        return self.totale() / len(self.vendite)

# vendite sopra la media
    def sopra_media(self):
        media_vendite = self.media()
        risultato = []
        giorno = 1  
        for valore in self.vendite:
            if valore > media_vendite:
                risultato.append((giorno, valore))
            giorno += 1
        return risultato
