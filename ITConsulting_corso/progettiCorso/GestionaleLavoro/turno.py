class Turno:
    #Classe per gestire un turno di lavoro

    def __init__(self, orario_entrata: str, orario_uscita: str, tipo: str = "normale"):
        
        self.__orario_entrata = orario_entrata
        self.__orario_uscita = orario_uscita
        self.__tipo = tipo  

    # GETTER e SETTER
    def get_orario_entrata(self):
        return self.__orario_entrata

    def set_orario_entrata(self, ora: str):
        self.__orario_entrata = ora

    def get_orario_uscita(self):
        return self.__orario_uscita

    def set_orario_uscita(self, ora: str):
        self.__orario_uscita = ora

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo: str):
        self.__tipo = tipo

    # METODI
    def controllo_orario(self, ora_corrente: str) -> bool:
        # polimorfismo
        if self.__tipo.lower() == "notturno":
            # scelta di un orario
            return self.__orario_entrata <= ora_corrente <= "23:59" or "00:00" <= ora_corrente <= self.__orario_uscita
        return self.__orario_entrata <= ora_corrente <= self.__orario_uscita

    def durata_turno(self) -> int:
        # calcola una durata
        entrata_h, entrata_m = map(int, self.__orario_entrata.split(":"))
        uscita_h, uscita_m = map(int, self.__orario_uscita.split(":"))
        ore = uscita_h - entrata_h
        minuti = uscita_m - entrata_m
        if minuti < 0:
            minuti += 60
            ore -= 1
        return ore + minuti / 60

    def info_turno(self) -> str:
        return f"Turno {self.__tipo}: {self.__orario_entrata} - {self.__orario_uscita} ({self.durata_turno():.2f} h)"
