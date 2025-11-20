class Teatro:
    
    def __init__(self):
        self._posti = []
        
    def aggiungi_posto(self, posto):
        self._posti.append(posto)
        
    def prenota_posto(self, numero: int, fila: str):
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota() 
                return 
        print(f"posto della {fila} {numero} non trovato")
        
        
    def stampa_posti_occupati(self):
        print("\nPosti occupati:")
        nessun_occupato = False
        for posto in self._posti:
            if posto.is_occupato():
                print(f"- {posto.get_fila()}{posto.get_numero()}")
                nessun_occupato = True
        if not nessun_occupato:
            print("Nessun posto occupato.")

# NON TERMINATO
        

