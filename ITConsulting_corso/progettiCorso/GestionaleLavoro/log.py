class LogIngresso:

    def __init__(self):
        self.__eventi = []  # log positivi (entrate/uscite)
        self.__errori = []  # log accessi negati o fuori orario

   
    # Registrazione entrata
   
    def registra_entrata(self, dipendente):
        """Duck typing: dipendente deve avere get_nome_completo()"""
        self.__eventi.append(f"{dipendente.get_nome_completo()} entrato")

   
    # Registrazione uscita
   
    def registra_uscita(self, dipendente):
        self.__eventi.append(f"{dipendente.get_nome_completo()} uscito")

  
    # Registrazione tentativo negato
  
    def registra_errore(self, messaggio: str):
        self.__errori.append(messaggio)

    # -----------------------------
   # report completo
    # -----------------------------
    def mostra_report(self):
        print("\n=== REPORT ENTRATE/USCITE ===")
        for evento in self.__eventi:
            print(evento)
        print("\n=== TENTATIVI NEGATI ===")
        for errore in self.__errori:
            print(errore)
        print("\n============================\n")

  # filtraggio dei ruoli 
    def filtra_errori_per_ruolo(self, ruolo_nome: str):
        #Mostra solo errori relativi a un ruolo specifico
        filtered = [e for e in self.__errori if ruolo_nome.lower() in e.lower()]
        print(f"=== ERRORI per ruolo {ruolo_nome} ===")
        for e in filtered:
            print(e)
        print("===============================")

    def filtra_eventi_per_ora(self, ora: str):
        filtered = [e for e in self.__eventi if ora in e]
        print(f"=== EVENTI all'ora {ora} ===")
        for e in filtered:
            print(e)
        print("===============================")

    # GETTER
    def get_eventi(self):
        return self.__eventi

    def get_errori(self):
        return self.__errori
