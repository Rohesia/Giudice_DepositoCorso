# ----------------------------
# Main
# ----------------------------
from menu import *
from funzioni import *



def main():
    menu = Menu("Gestione Impiegati")
    menu.aggiungi_voce(MenuItem("Aggiungi Impiegato Fisso", "Inserisci un impiegato con stipendio fisso", aggiungi_fisso))
    menu.aggiungi_voce(MenuItem("Aggiungi Impiegato a Provvigione", "Inserisci un impiegato con stipendio + bonus vendite", aggiungi_provvigione))
    menu.aggiungi_voce(MenuItem("Mostra Impiegati", "Visualizza tutti gli impiegati con stipendio calcolato", mostra_impiegati))
    menu.aggiungi_voce(MenuItem("Aggiungi Impiegato con Rimborso", "Inserisci un impiegato con stipendio + rimborso", aggiungi_rimborso))
    menu.seleziona()

if __name__ == "__main__":
    main()