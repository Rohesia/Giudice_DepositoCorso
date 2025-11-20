# -------------------
# Officina
# -------------------

from menu import * 
from lavatrice import Lavatrice
from forno import Forno 
from ticket import TicketRiparazione 
from frigorifero import Frigorifero 

class Officina:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__tickets = []

    # --- getter ---
    def get_nome(self) -> str:
        return self.__nome

    # --- gestione tickets ---
    def aggiungi_ticket(self, ticket):
        if ticket is None:
            print("Errore: ticket non valido")
            return
        self.__tickets.append(ticket)

    def chiudi_ticket(self, id_ticket: int) -> bool:
        # Chiude il ticket con id specificato; ritorna True se trovato e chiuso
        for t in self.__tickets:
            if t.get_id_ticket() == id_ticket:
                t.set_stato("chiuso")
                return True
        print("Attenzione: ticket non trovato")
        return False

    def stampa_ticket_aperti(self):
        print(f"Ticket aperti in '{self.__nome}':")
        for t in self.__tickets:
            if t.get_stato() == "aperto":
                ele = t.get_elettrodomestico()
                if ele is not None:
                    print(f"- ID: {t.get_id_ticket()} | Tipo: {type(ele).__name__} | {ele.descrizione()}")

    def totale_preventivi(self) -> float:
        # Somma i preventivi di tutti i ticket (solo costo base)
        totale = 0.0
        for t in self.__tickets:
            ele = t.get_elettrodomestico()
            if ele is not None:
                totale += float(ele.stima_costo_base())
        return totale

    def conta_per_tipo(self) -> dict:
        # Conteggia le sottoclassi Lavatrice, Frigorifero, Forno, Altro usando isinstance
        counts = {"Lavatrice": 0, "Frigorifero": 0, "Forno": 0, "Altro": 0}
        for t in self.__tickets:
            ele = t.get_elettrodomestico()
            if ele is None:
                counts["Altro"] += 1
            elif isinstance(ele, Lavatrice):
                counts["Lavatrice"] += 1
            elif isinstance(ele, Frigorifero):
                counts["Frigorifero"] += 1
            elif isinstance(ele, Forno):
                counts["Forno"] += 1
            else:
                counts["Altro"] += 1
        return counts

    def riepilogo(self):
        # Stampa un riepilogo dell'officina
        total_opened = len(self.__tickets)
        counts = self.conta_per_tipo()
        stati = {"aperto": 0, "in lavorazione": 0, "chiuso": 0}
        for t in self.__tickets:
            stato = t.get_stato()
            if stato in stati:
                stati[stato] += 1
            else:
                stati[stato] = 1

        totale_preventivi = self.totale_preventivi()

        print(f"--- RIEPILOGO OFFICINA: {self.__nome} ---")
        print(f"Ticket totali: {total_opened}")
        print(f"Conteggi per tipo: {counts}")
        print(f"Stati ticket: {stati}")
        print(f"Totale stimato dei preventivi (solo costo base): {totale_preventivi:.2f} €")
