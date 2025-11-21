class Badge:
    #Classe che rappresenta il badge di un dipendente

    def __init__(self, id_badge: int, livello_accesso: list[str] = None):
        
        self.__id_badge = id_badge
        self.__attivo = True
        self.__livello_accesso = livello_accesso if livello_accesso else []
        self.__log_accessi = []  

    # INCAPSULAMENTO: getter/setter
    def get_id_badge(self):
        return self.__id_badge

    def set_id_badge(self, id_badge: int):
        self.__id_badge = id_badge

    def get_attivo(self):
        return self.__attivo

    def set_attivo(self, stato: bool):
        self.__attivo = stato

    def get_livello_accesso(self):
        return self.__livello_accesso

    def set_livello_accesso(self, aree: list[str]):
        self.__livello_accesso = aree

    def get_log_accessi(self):
        return self.__log_accessi

    # metodi
    def attiva(self):
        self.__attivo = True
        print(f"Badge {self.__id_badge} attivato")

    def disattiva(self):
        self.__attivo = False
        print(f"Badge {self.__id_badge} disattivato")

    def verifica_accesso(self, area: str = None) -> bool:
        # controllo del badge
        if not self.__attivo:
            self.__log_accessi.append(f"Accesso negato: badge disattivato per area {area}")
            return False
        if area and area.lower() not in (a.lower() for a in self.__livello_accesso):
            self.__log_accessi.append(f"Accesso negato: area {area} non consentita")
            return False
        self.__log_accessi.append(f"Accesso consentito per area {area}")
        return True

    # mostra log degli accessi
    def mostra_log(self):
        print(f"--- Log badge {self.__id_badge} ---")
        for evento in self.__log_accessi:
            print(evento)
        print("------------------------------")
