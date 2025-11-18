from Libreria import *

class Libro:
    def __init__(self, titolo: str, autore: str, isbn: str) -> None: 
        self.titolo = titolo 
        self.autore = autore 
        self.isbn = isbn 
        
    def descrizione(self) -> str:
        return f"Il libro '{self.titolo}' di {self.autore} possiede ISBN: {self.isbn}"

