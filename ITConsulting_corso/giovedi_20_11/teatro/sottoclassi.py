from posto import Posto


# classe PostoVIP
class PostoVIP(Posto):
    # posto con servizi extra
    
    servizi_disponibili = {
        "lounge": "Accesso al lounge VIP",
        "parcheggio": "Parcheggio riservato",
        "servizio_posto": "Servizio food & beverage al posto",
        "priorita": "Ingresso prioritario",
        "cloakroom": "Guardaroba dedicato"
    }

    def __init__(self, numero:int, fila: str, servizi_extra=None):
        super().__init__(numero, fila)
        
        # se non vengono specificati vengono attivati tutti 
        if servizi_extra is None:
            self._servizi_extra = list(self.servizi_disponibili.keys())
        else:
            self._servizi_extra = self._valida_servizi(servizi_extra)
            
        
    def valida_servizi(self, servizi):
        servizi_validi = []
        for s in servizi:
            s_lower = s.lower().strip()
            if s_lower not in self.servizi_disponibili:
                print(f"{s} non disponibile. Servizi validi: {', '.join(self.servizi_disponibili.keys())}")
            else:
                servizi_validi.append(s_lower)
        return servizi_validi
                

    def prenota(self) -> bool:
        if self.is_occupato():
            print(f"Posto VIP {self.get_fila()}{self.get_numero()} già occupato!")
            return False
        
        super().prenota()
        
        if self.servizi_extra:
            print(f"Servizi extra attivati")
            for servizio in self._servizi_extra:
                print(f" {self.servizi_disponibili[servizio]}")
        
        return True
    
    def __str__(self) -> str:
        stato = "OCCUPATO" if self.is_occupato() else "LIBERO"
        return f"Posto Standard {self.get_fila()}{self.get_numero()} [{stato}] - {self.costo:.2f}€"

    
    def __repr__(self) -> str:
        return (f"PostoVIP(numero={self.get_numero()}, fila='{self.get_fila()}', "
                f"servizi={self._servizi_extra}, occupato={self.is_occupato()})")
    
    

class PostoStandard(Posto):

    def __init__(self, numero: int, fila: str, costo: float = 0):
        super().__init__(numero, fila)
        self.costo = costo

    def prenota(self):
        if not self.is_occupato():
            
            super().prenota()
            
            print(f"Costo prenotazione: {self.costo:.2f}€")
        else:
            print(f"Posto Standard {self.get_fila()}{self.get_numero()} già occupato.")
            
            
    def __str__(self) -> str:
        stato = "OCCUPATO" if self.is_occupato() else "LIBERO"
        return (f"Posto Standard {self.get_fila()}{self.get_numero()} [{stato}] - "
                f"{self._costo:.2f}€")
    
    def __repr__(self) -> str:
        return (f"PostoStandard(numero={self.get_numero()}, fila='{self.get_fila()}', "
                f"costo={self._costo}, occupato={self.is_occupato()})")
        
        
        
        
# NON TERMINATO