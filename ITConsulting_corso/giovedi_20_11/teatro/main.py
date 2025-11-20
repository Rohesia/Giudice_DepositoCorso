from teatro import Teatro
from sottoclassi import PostoVIP, PostoStandard
from menu import *

# --- Funzione di avvio menu teatro ---
def avvia_menu_teatro(teatro: Teatro):

    def prenota_posto():
        fila = input("Inserisci la fila del posto: ").strip().upper()
        numero = input("Inserisci il numero del posto: ").strip()
        if numero.isdigit():
            teatro.prenota_posto(int(numero), fila)
        else:
            print("Numero non valido.")

    def libera_posto():
        fila = input("Inserisci la fila del posto da liberare: ").strip().upper()
        numero = input("Inserisci il numero del posto da liberare: ").strip()
        if numero.isdigit():
            for posto in teatro._posti:
                if posto.get_fila() == fila and posto.get_numero() == int(numero):
                    posto.libera()
                    return
            print(f"Posto {fila}{numero} non trovato.")
        else:
            print("Numero non valido.")

    def visualizza_occupati():
        teatro.stampa_posti_occupati()

    # Creazione menu
    menu = Menu("Gestione Teatro")
    menu.aggiungi_voce(MenuItem("Prenota posto", "Prenota un posto disponibile", prenota_posto))
    menu.aggiungi_voce(MenuItem("Libera posto", "Libera un posto precedentemente prenotato", libera_posto))
    menu.aggiungi_voce(MenuItem("Visualizza posti occupati", "Mostra tutti i posti attualmente occupati", visualizza_occupati))

    # Avvio menu
    menu.seleziona()


# --- Esempio di utilizzo ---
if __name__ == "__main__":
    teatro = Teatro()
    # Aggiunta posti demo
    teatro.aggiungi_posto(PostoStandard(1, "A", costo=50))
    teatro.aggiungi_posto(PostoStandard(2, "A", costo=50))
    teatro.aggiungi_posto(PostoVIP(1, "V", servizi_extra=["Accesso al lounge", "Servizio in posto"]))

    avvia_menu_teatro(teatro)
    
    
# NON TERMINATO
