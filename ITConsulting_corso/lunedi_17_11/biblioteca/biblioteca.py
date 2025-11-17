# ==========================================================
# CLASSE BIBLIOTECA
# ==========================================================
class Biblioteca:
    def __init__(self):
        # lista dei libri
        self.libri = []

    # inserimento
    def inserisci(self, libro):
        self.libri.append(libro)
        print(f"Libro inserito: {libro.titolo}")

    # stampare tutti i libri usando __str__
    def stampa_biblioteca(self):
        if not self.libri:
            print("La biblioteca è vuota.")
        else:
            print("\nLibri presenti in biblioteca:")
            for libro in self.libri:
                print(libro)

    # stampare tutte le descrizioni 
    def stampa_descrizioni(self):
        if not self.libri:
            print("La biblioteca è vuota.")
        else:
            print("\nDescrizione dei libri:")
            for libro in self.libri:
                libro.descrizione()
