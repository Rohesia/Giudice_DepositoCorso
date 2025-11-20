from menu import Menu, MenuItem
from lavatrice import Lavatrice
from forno import Forno
from frigorifero import Frigorifero
from ticket import TicketRiparazione
from officina import Officina
def main():
    # --- Creazione officina ---
    officina = Officina("Officina Centrale")
    ticket_counter = [1]  # contatore ID ticket

    # --- Funzioni menu ---
    def aggiungi_ticket_demo():
        print("\n--- Aggiunta Ticket Demo ---")
        demo_elettro = [
            Lavatrice("Whirlpool", "W123", 2020, "Non centrifuga", 8, 1200),
            Frigorifero("Samsung", "SFridge", 2019, "Non raffredda", 350, True),
            Forno("Ariston", "F200", 2022, "Non si accende", "elettrico")
        ]
        for ele in demo_elettro:
            t_id = ticket_counter[0]
            ticket = TicketRiparazione(t_id, ele)
            officina.aggiungi_ticket(ticket)
            print(f"Ticket ID {t_id} aggiunto: {type(ele).__name__} - {ele.descrizione()}")
            ticket_counter[0] += 1

    def mostra_ticket_aperti():
        print("\n--- Ticket Aperti ---")
        officina.stampa_ticket_aperti()

    def chiudi_ticket_demo():
        t_id_input = input("Inserisci ID ticket da chiudere: ").strip()
        if not t_id_input.isdigit():
            print("Errore: devi inserire un numero intero")
            return
        t_id = int(t_id_input)
        successo = officina.chiudi_ticket(t_id)
        if successo:
            print(f"Ticket ID {t_id} chiuso con successo!")
        else:
            print("Ticket non trovato.")

    def modifica_attributi():
        print("\n--- Modifica Attributi Elettrodomestico ---")
        # Lista ticket con ID
        for t in officina._Officina__tickets:
            ele = t.get_elettrodomestico()
            print(f"{t.get_id_ticket()}: {type(ele).__name__} - {ele.descrizione()}")
        
        t_id_input = input("Seleziona ID ticket per modificare: ").strip()
        if not t_id_input.isdigit():
            print("Errore: inserisci un numero valido")
            return
        t_id = int(t_id_input)

        # Trova ticket
        ticket = None
        for t in officina._Officina__tickets:
            if t.get_id_ticket() == t_id:
                ticket = t
                break
        if ticket is None:
            print("Ticket non trovato")
            return

        ele = ticket.get_elettrodomestico()
        if isinstance(ele, Lavatrice):
            nuovo_kg = input("Inserisci nuovo kg: ").strip()
            nuovo_giri = input("Inserisci nuovi giri centrifuga: ").strip()
            if nuovo_kg.isdigit():
                ele.set_kg(int(nuovo_kg))
            if nuovo_giri.isdigit():
                ele.set_giri_centrifuga(int(nuovo_giri))
        elif isinstance(ele, Frigorifero):
            nuovo_litri = input("Inserisci nuovi litri: ").strip()
            freezer = input("Ha freezer? (s/n): ").strip().lower()
            if nuovo_litri.isdigit():
                ele.set_litri(int(nuovo_litri))
            if freezer == "s":
                ele.set_ha_freezer(True)
            elif freezer == "n":
                ele.set_ha_freezer(False)
        elif isinstance(ele, Forno):
            tipo = input("Tipo alimentazione (elettrico/gas): ").strip().lower()
            ele.set_tipo_alimentazione(tipo)
        
        print("Modifica completata:")
        print(ele.descrizione())

    def riepilogo_officina():
        print("\n--- Riepilogo Officina ---")
        officina.riepilogo()

    # --- Creazione menu ---
    menu = Menu("Menu Officina")
    menu.aggiungi_voce(MenuItem("Aggiungi Ticket Demo", "Crea ticket demo", aggiungi_ticket_demo))
    menu.aggiungi_voce(MenuItem("Mostra Ticket Aperti", "Visualizza tutti i ticket aperti", mostra_ticket_aperti))
    menu.aggiungi_voce(MenuItem("Chiudi Ticket", "Chiude un ticket specificato", chiudi_ticket_demo))
    menu.aggiungi_voce(MenuItem("Modifica Attributi", "Modifica attributi elettrodomestici tramite setter", modifica_attributi))
    menu.aggiungi_voce(MenuItem("Riepilogo Officina", "Mostra riepilogo completo", riepilogo_officina))

    # --- Avvio menu ---
    menu.seleziona()


if __name__ == "__main__":
    main()
