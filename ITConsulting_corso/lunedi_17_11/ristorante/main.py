from ristorante import *

# creazione di oggetti
ristorante1 = Ristorante("Burger House", "Americana")
ristorante2 = Ristorante("Bella italia", "Italiana")

# creazione del dizionario
ristoranti = {
    ristorante1.nome: ristorante1,
    ristorante2.nome: ristorante2
}

# metodi per i dizionari
for nome, ristorante in ristoranti.items():
    print(f"\n--- {nome} ---")
    ristorante.descrivi_ristorante()
    ristorante.stato_apertura()
    ristorante.apri_ristorante()
    ristorante.stato_apertura()


# metodo per aggiunta menu
ristoranti["Burger House"].aggiungi_al_menu("Cheeseburger", 6.5)
ristoranti["Burger House"].aggiungi_al_menu("Hamburger Classico", 5.5)
ristoranti["Burger House"].aggiungi_al_menu("Patatine Fritte", 3.0)
ristoranti["Bella italia"].aggiungi_al_menu("Onion Rings", 4.0)
ristoranti["Bella italia"].aggiungi_al_menu("Milkshake alla Vaniglia", 4.5)

# stampa dei menu
for nome, ristorante in ristoranti.items():
    print(f"\nMenu del ristorante '{nome}':")
    ristorante.stampa_menu()

# rimozione
ristoranti["Burger House"].togli_dal_menu("Hamburger Classico")
ristoranti["Burger House"].stampa_menu()

# chiudere
for ristorante in ristoranti.values():
    ristorante.chiudi_ristorante()
    ristorante.stato_apertura()
