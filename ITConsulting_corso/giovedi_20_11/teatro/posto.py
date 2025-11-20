# classe base posto 
# classe base per un posto al teatro
class Posto: 
    def __init__(self, numero:int, fila:str):
        self._numero = numero
        self._fila = fila
        self._occupato = False 
        
    # prenotazione del posto solo se questo è libero
    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto in {self._fila} con {self._numero} prenotato")
        else: 
            print(f"Posto {self._fila}{self._numero} già occupato!")
            
    # gestione del posto libero
    def libera(self): 
        if self._occupato: 
            self._occupato = False 
            print(f"posto {self._numero} in {self._fila} libero")
        else: 
            print(f" il posto {self._fila}{self._numero} non era prenotato.")
            
    # get 
    def get_numero(self) -> int: 
        return self._numero 
    
    def get_fila(self) -> str:
        return self._fila 
    
    def  is_occupato(self) -> bool: 
        return self._occupato 
    
    
        
        