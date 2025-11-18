from audiolibro import * 
from film import * 
from multimediali import * 

# gestione biblioteca multimediale
class BibliotecaMultimediale:

    def __init__(self):
        # creazione lista per il catalogo
        self.catalogo = []

    def aggiungi_elemento(self, elemento):
        # aggiunta del libro 
        self.catalogo.append(elemento)

    def rimuovi_elemento_per_titolo(self, titolo):
        # rimozione libro
        trovato = False
        nuovo_catalogo = []

        i = 0
        while i < len(self.catalogo):
            elem = self.catalogo[i]
            # case-insensitive
            if not trovato and elem.titolo.lower() == titolo.lower():
                trovato = True
            else:
                nuovo_catalogo.append(elem)
            i += 1

        self.catalogo = nuovo_catalogo
        return trovato
    
    def cerca_per_genere(self, genere):
        # ricera 
        risultati = []
        for elem in self.catalogo:
            if elem.genere.lower() == genere.lower():
                risultati.append(elem)
        return risultati

    def cerca_per_autore(self, autore):
        # lista di libri in base all'autore
        risultati = []
        for elem in self.catalogo:
            if elem.autore.lower() == autore.lower():
                risultati.append(elem)
        return risultati

    def cerca_parola_chiave(self, parola):
        # avvio la ricerca slla base di una parola chiave
        risultati = []
        for elem in self.catalogo:
            if parola.lower() in elem.titolo.lower():
                risultati.append(elem)
        return risultati
    
    
# NON ANCORA TERMINATO