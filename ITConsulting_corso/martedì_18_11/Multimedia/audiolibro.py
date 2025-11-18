class Audiolibro:
    def __init__(self, titolo: str, autore: str, anno_pubblicazione: int,
                 genere: str, durata_minuti: int, narratore: str) -> None:
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione
        self.genere = genere
        self.durata_minuti = durata_minuti
        self.narratore = narratore

    def descrizione(self) -> str:
        return (f"Audiolibro: '{self.titolo}' di {self.autore}, {self.anno_pubblicazione}, "
                f"Genere: {self.genere}, Durata: {self.durata_minuti} min, "
                f"Narratore: {self.narratore}")