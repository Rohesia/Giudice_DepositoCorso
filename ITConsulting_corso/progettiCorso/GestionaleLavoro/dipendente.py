# =========================================
# DIPENDENTE: eredita da Persona e implementa Accesso
# =========================================
from badge import Badge
from turno import Turno
from log import LogIngresso
from persona import Persona

class Dipendente(Persona, Persona.Accesso):
    #Classe concreta che rappresenta un dipendente

    def __init__(self, nome: str, cognome: str, cf: str, ruolo, badge: Badge, turni: list):
        super().__init__(nome, cognome, cf)
        self.__ruolo = ruolo
        self.__badge = badge
        self.__turni = turni  

    # polimorfismo = duck typing
    def entra_in_azienda(self, ora_corrente: str, log: LogIngresso):
        if not self.__badge:
            log.registra_errore(f"{self.get_nome_completo()} non ha badge")
            return
        if not self.__badge.verifica_accesso():
            log.registra_errore(f"Accesso negato a {self.get_nome_completo()}")
            self.avvisa_supervisore()
            return
        turno_valido = any(t.controllo_orario(ora_corrente) for t in self.__turni)
        if not turno_valido:
            log.registra_errore(f"{self.get_nome_completo()} fuori orario")
            self.avvisa_supervisore()
            return
        log.registra_entrata(self)

    def esce_dall_azienda(self, log: LogIngresso):
        log.registra_uscita(self)

    # simula una giornata tipo lavorativa
    def simula_giornata(self, log: LogIngresso, orari: list[str]):
        #Simula l'ingresso e uscita per tutti gli orari della giornata
        for ora in orari:
            if any(t.controllo_orario(ora) for t in self.__turni):
                self.entra_in_azienda(ora, log)
            else:
                self.esce_dall_azienda(ora, log)
                

    def avvisa_supervisore(self):
        #avvisa se c'è un accesso fuori orario o negato
        print(f"*** Il Supervisore è stato avvisato: {self.get_nome_completo()} ha tentato un accesso non autorizzato ***")

    # POLIMORFISMO: implementa il metodo astratto info()
    def info(self) -> str:
        ruolo_nome = self.__ruolo.get_nome_ruolo() if self.__ruolo else "Ruolo non definito"
        return f"{self.get_nome_completo()}, ruolo: {ruolo_nome}"

    # GETTER e SETTER
    def get_ruolo(self):
        return self.__ruolo

    def set_ruolo(self, ruolo):
        self.__ruolo = ruolo

    def get_badge(self):
        return self.__badge

    def set_badge(self, badge: Badge):
        self.__badge = badge

    def get_turni(self):
        return self.__turni
    
    def set_turni(self, turni: list):
        self.__turni = turni