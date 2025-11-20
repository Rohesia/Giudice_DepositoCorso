# classe base per un posto al teatro
class Posto: 
    def __init__(self, numero: int, fila: str):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = False 
        
    # prenotazione del posto solo se questo è libero
    def prenota(self):
        if not self.__occupato:
            self.__occupato = True
            print(f"Posto in {self.__fila} con {self.__numero} prenotato")
        else: 
            print(f"Posto {self.__fila}{self.__numero} già occupato!")
            
    # gestione del posto libero
    def libera(self): 
        if self.__occupato: 
            self.__occupato = False 
            print(f"Posto {self.__fila}{self.__numero} libero")
        else: 
            print(f"Il posto {self.__fila}{self.__numero} non era prenotato.")
            
    # getter
    def get_numero(self) -> int: 
        return self.__numero 
    
    def get_fila(self) -> str:
        return self.__fila 
    
    def is_occupato(self) -> bool: 
        return self.__occupato
