
from libro import *
from biblioteca import *

biblioteca = Biblioteca()

# creazione oggetti
libro1 = Libro("Romeo e Giulietta", "William Shakespeare", 160)
libro2 = Libro("L'interpretazione dei sogni", "Sigmund Freud", 634)
libro3 = Libro("I dolori del giovane Werther", "Johann Wolfgang von Goethe", 352)

# aggiungo i libri alla biblioteca
biblioteca.inserisci(libro1)
biblioteca.inserisci(libro2)
biblioteca.inserisci(libro3)

print("\nStampo tutti i libri nella biblioteca:")
biblioteca.stampa_biblioteca()


print("\Descrizione dei libri con spaziatori:")
biblioteca.stampa_descrizioni()