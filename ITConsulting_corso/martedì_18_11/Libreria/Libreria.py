from Libro import Libro


class Libreria:
    def __init__(self) -> None:
        self.catalogo = []

    def aggiungi_libro(self, libro: Libro) -> None:
        self.catalogo.append(libro)

    def rimuovi_libro(self, isbn: str) -> bool:
        nuovo_catalogo = []
        trovato = False

        for libro in self.catalogo:
            if libro.isbn == isbn:
                trovato = True  
            else:
                nuovo_catalogo.append(libro)

        self.catalogo = nuovo_catalogo
        return trovato

    def cerca_per_titolo(self, titolo: str) -> list:
        risultati = []
        for libro in self.catalogo:
            if libro.titolo == titolo:
                risultati.append(libro)
        return risultati

    def mostra_catalogo(self) -> None:
        if not self.catalogo:
            print("Il catalogo è vuoto")
            return

        print("Catalogo libreria:")
        for libro in self.catalogo:
            print("-", libro.descrizione())