from Libro import Libro
from Libreria import Libreria

def utilizzo():
    # Creo libri
    libro1 = Libro("1984", "George Orwell", "123")
    libro2 = Libro("1984", "Mario Rossi", "999")
    libro3 = Libro("Il piccolo principe", "Saint-Exupéry", "555")

    # Creo libreria e aggiungo libri
    mia_libreria = Libreria()
    mia_libreria.aggiungi_libro(libro1)
    mia_libreria.aggiungi_libro(libro2)
    mia_libreria.aggiungi_libro(libro3)

    # Mostro catalogo
    descrizioni = mia_libreria.mostra_catalogo()
    print("Catalogo libreria:")
    for d in descrizioni:
        print("-", d)

    # Cerco libri per titolo
    risultati = mia_libreria.cerca_per_titolo("1984")
    for r in risultati:
        print("Trovato:", r.descrizione())

    # Rimuovo un libro
    rimosso = mia_libreria.rimuovi_libro("999")
    print(f"Libro con ISBN {rimosso} rimosso")

    # Mostro catalogo aggiornato
    descrizioni = mia_libreria.mostra_catalogo()
    print("Catalogo aggiornato:")
    for d in descrizioni:
        print("-", d)


utilizzo()
