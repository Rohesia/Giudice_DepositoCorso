from metodopagamento import MetodoPagamento

#Classe Carta di credito
class CartaDiCredito(MetodoPagamento):
    __numero_carta: str = "0000-1111-2222-3333"
    __intestatario: str = "Cliente"
    
    
    def effettua_pagamento(self, importo: float) -> bool:
        if importo <= 0:
            print("Importo non valido")
        print(f"Pagamento di {importo:.2f}€ effettuato...")
        return True
    
    def get_intestatario(self) -> str:
        return self.__intestatario 
    
    def get_numero_carta(self) -> str:
        return self.__numero_carta
    
    def set_intestatario(self, valore: str) -> None:
        self.__intestatario = valore 
        
    def __str__(self) -> str:
        return f"Carta di credito appartenente a {self.__intestatario}"
    

    
    
    
    
# Classe PayPal 
class PayPal(MetodoPagamento):
    __email: str = "ciao@ciao.com"
    
    def effettua_pagamento(self, pagamento: float) -> bool:
        print(f"Pagamento di {pagamento:.2f}€ effettuato tramite PayPal ({self.__email}).")
        return True
    
    def get_email(self) -> str:
        return self.__email 
    
    def set__email(self, valore: str) -> None:
        self.__email = valore 
        
    def __str__(self) -> str:
        return f"PayPal email = {self.__email}"  
    
    
# Classe BonificoBancario 
class BonificoBancario(MetodoPagamento):
    __iban: str = "IT00A0000000000000000000000"
    
    def effettua_pagamento(self, pagamento: float)-> bool:
        print(f"Pagamento di {pagamento:.2f}€ effettuato tramite Bonifico Bancario (IBAN: {self.__iban}).")
        return True
    
    def get_iban(self)-> str:
        return f"Bonifico Bancario con IBAN= {self.__iban}"