class Libro:
    def __init__(self, titolo: str, autore: str, anno_pubblicazione: int, genere: str) -> None:
        self.titolo = titolo 
        self.autore = autore 
        self.anno_pubblicazione = anno_pubblicazione
        self.genere = genere 
        
    def descrizione(self):
        return (f"Libro: '{self.titolo}' di {self.autore}, {self.anno_pubblicazione}, "
                f"Genere: {self.genere}")
        
        
        
        
    