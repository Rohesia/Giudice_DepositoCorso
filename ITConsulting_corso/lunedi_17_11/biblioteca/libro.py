# ==========================================================
# CLASSE LIBRO
# ==========================================================

# decoratore 
def spaziatore(func):
    def wrapper(*args, **kwargs):
        print("-" * 50)  
        risultato = func(*args, **kwargs)
        print(risultato)  
        print("-" * 50)  
        return risultato
    return wrapper


# Classe Libro
class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    # metodo descrizione 
    @spaziatore
    def descrizione(self):
        return f"Il libro '{self.titolo}' è stato scritto da {self.autore} e ha {self.pagine} pagine."

    def __str__(self):
        return f"Libro(titolo='{self.titolo}', autore='{self.autore}', pagine={self.pagine})"


