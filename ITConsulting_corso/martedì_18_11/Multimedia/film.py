class Film:
    def __init__(self, titolo: str, regista: str, anno_pubblicazione: int,
                 genere: str, durata_minuti: int, vietato_ai_minori: bool) -> None:
        self.titolo = titolo
        self.autore = regista  
        self.anno_pubblicazione = anno_pubblicazione
        self.genere = genere
        self.durata_minuti = durata_minuti
        self.vietato_ai_minori = vietato_ai_minori
        
    def descrizione(self) -> str:
        vietato = "Sì" if self.vietato_ai_minori else "No"
        return (f"Film: '{self.titolo}' di {self.autore}, {self.anno_pubblicazione}, "
                f"Genere: {self.genere}, Durata: {self.durata_minuti} min, "
                f"Vietato ai minori: {vietato}")
        
    
            
        