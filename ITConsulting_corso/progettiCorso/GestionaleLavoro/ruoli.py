from abc import ABC, abstractmethod

# =========================================
# ASTRAZIONE: Ruolo base astratto
# Non istanziabile direttamente
# =========================================
class Ruolo(ABC):
    #Classe astratta che rappresenta un ruolo aziendale

    def __init__(self, nome_ruolo: str):
        self.__nome_ruolo = nome_ruolo

    # GETTER e SETTER
    def get_nome_ruolo(self):
        return self.__nome_ruolo

    def set_nome_ruolo(self, nome: str):
        self.__nome_ruolo = nome

    @abstractmethod
    def autorizzazioni(self) -> list[str]:
        #Metodo astratto da implementare nelle sottoclassi
        pass

    # controlla se può accedere a una determinata area
    def puo_accedere(self, area: str) -> bool:
        #Verifica se il ruolo ha l'autorizzazione per una determinata area
        return area.lower() in (perm.lower() for perm in self.autorizzazioni())


# =========================================
# EREDITA' e POLIMORFISMO
# Ogni ruolo ha autorizzazioni diverse
# =========================================
class Manager(Ruolo):
    def autorizzazioni(self) -> list[str]:
        return ["uffici", "archivi", "team"]

    #  manager può modificare i turni dei dipendenti
    def modifica_turno(self, dipendente, nuovo_turno):
        dipendente.set_turni([nuovo_turno])
        print(f"{dipendente.get_nome_completo()} ora ha nuovo turno: {nuovo_turno.get_orario_entrata()} - {nuovo_turno.get_orario_uscita()}")


class Operaio(Ruolo):
    def autorizzazioni(self) -> list[str]:
        return ["produzione"]

    # operaio può segnalare guasti
    def segnala_guasto(self, area: str):
        print(f"Guasto segnalato nell'area {area} da un operaio")


class Security(Ruolo):
    def autorizzazioni(self) -> list[str]:
        return ["uffici", "archivi", "produzione", "laboratori"]

    #  security può bloccare badge
    def blocca_badge(self, badge):
        badge.disattiva()
        print(f"Badge {badge.get_id_badge()} disattivato da Security")
