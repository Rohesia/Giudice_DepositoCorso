from gestore_pagamenti import GestorePagamenti
from sottoclassi import CartaDiCredito, PayPal, BonificoBancario

# --- Menu dinamico ---
class MenuItem:
    def __init__(self, nome, descrizione, azione):
        self.nome = nome
        self.descrizione = descrizione
        self.azione = azione

    def esegui(self):
        self.azione()

    def __str__(self):
        return f"{self.nome}: {self.descrizione}"


class Menu:
    def __init__(self, titolo, voci=None):
        self.titolo = titolo
        self.voci = voci if voci is not None else []

    def aggiungi_voce(self, voce):
        self.voci.append(voce)

    def mostra(self):
        print(f"\n=== {self.titolo} ===")
        for idx, voce in enumerate(self.voci, start=1):
            print(f"{idx}. {voce}")
        print(f"{len(self.voci)+1}. Esci")

    def seleziona(self):
        while True:
            self.mostra()
            scelta = input("Seleziona un'opzione: ").strip()
            if not scelta.isdigit():
                print("Input non valido. Inserisci un numero.")
                continue
            indice = int(scelta)
            if indice == len(self.voci)+1:
                print("Uscita dal menu.")
                break
            elif 1 <= indice <= len(self.voci):
                self.voci[indice-1].esegui()
            else:
                print("Opzione non valida. Riprova.")


# --- Funzione principale che esegue il menu ---
def avvia_menu_pagamenti(importo: float = 150.0):
    # Creazione dei metodi di pagamento
    carta = CartaDiCredito()
    paypal = PayPal()
    bonifico = BonificoBancario()
    gestore = GestorePagamenti(carta)

    # Funzioni di azione
    def paga_carta():
        gestore.cambia_metodo(carta)
        gestore.paga(importo)

    def paga_paypal():
        gestore.cambia_metodo(paypal)
        gestore.paga(importo)

    def paga_bonifico():
        gestore.cambia_metodo(bonifico)
        gestore.paga(importo)

    # Creazione del menu
    menu_pagamenti = Menu("Gestione Pagamenti")
    menu_pagamenti.aggiungi_voce(MenuItem("Carta di Credito", "Paga con la tua carta", paga_carta))
    menu_pagamenti.aggiungi_voce(MenuItem("PayPal", "Paga tramite PayPal", paga_paypal))
    menu_pagamenti.aggiungi_voce(MenuItem("Bonifico", "Paga tramite Bonifico Bancario", paga_bonifico))

    # Avvio del menu
    menu_pagamenti.seleziona()


# --- Esecuzione diretta senza if __name__ ---
avvia_menu_pagamenti()
