# -------------------
# Ticket Riparazione
# -------------------
class TicketRiparazione:
    def __init__(self, id_ticket: int, elettrodomestico):
        # --- ID ticket ---
        if type(id_ticket) != int or id_ticket <= 0:
            print("Errore: id_ticket deve essere un intero positivo")
            self.__id_ticket = 1  # valore di default sicuro
        else:
            self.__id_ticket = id_ticket

        # --- Elettrodomestico ---
        self.__elettrodomestico = elettrodomestico  # assumiamo sia corretto

        # --- Stato e note ---
        self.__stato = "aperto"  # aperto, in lavorazione, chiuso
        self.__note = []

    # --- getter e setter ---
    def get_id_ticket(self) -> int:
        return self.__id_ticket

    def set_id_ticket(self, valore):
        if type(valore) != int or valore <= 0:
            print("Errore: id_ticket deve essere un intero positivo")
            return
        self.__id_ticket = valore

    def get_elettrodomestico(self):
        return self.__elettrodomestico

    def get_stato(self) -> str:
        return self.__stato

    def set_stato(self, valore):
        if valore != "aperto" and valore != "in lavorazione" and valore != "chiuso":
            print("Errore: stato non valido (deve essere 'aperto', 'in lavorazione' o 'chiuso')")
            return
        self.__stato = valore

    # --- gestione note ---
    def aggiungi_nota(self, testo):
        if type(testo) != str:
            print("Errore: nota deve essere una stringa")
            return
        self.__note.append(testo)

    def note(self):
        return list(self.__note)

    # --- calcolo preventivo ---
    def calcola_preventivo(self, *voci_extra):
        totale = 0.0
        totale = float(self.__elettrodomestico.stima_costo_base())
        
        for voce in voci_extra:
            if type(voce) == int or type(voce) == float:
                totale += float(voce)
            else:
                print("Errore: tutte le voci extra devono essere numeri (int o float) - voce ignorata")
            return totale


    # --- rappresentazione ---
    def __repr__(self):
        elettro_str = "Nessun elettrodomestico" if self.__elettrodomestico is None else self.__elettrodomestico.get_marca() + " " + self.__elettrodomestico.get_modello()
        return f"<Ticket {self.__id_ticket} - {elettro_str} - {self.__stato}>"
