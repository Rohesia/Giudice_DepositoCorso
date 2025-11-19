# -----------------------------
# Classe ContoBancario
# ----------------------------- 

class ContoBancario:
    def __init__(self, titolare: str, saldo_iniziale: float = 0.0):
        # Attributi privati
        self.__titolare = ""
        self.__saldo = 0.0
        
        # Uso del setter per validare/impostare il titolare
        self.set_titolare(titolare)
        
        # Se il saldo iniziale è positivo, lo deposito
        if saldo_iniziale > 0:
            self.deposita(saldo_iniziale)

     # Metodo per depositare denaro
    def deposita(self, importo: float) -> float:
        # Aggiunge l’importo se positivo
        if importo > 0:
            self.__saldo += importo
        return self.__saldo
    
    # Metodo per prelevare denaro
    def preleva(self, importo: float):
        # Preleva solo se l’importo è positivo e non supera il saldo
        if importo > 0 and importo <= self.__saldo:
            self.__saldo -= importo
            return self.__saldo
        
        # Se il prelievo non è valido, ritorna comunque il saldo attuale
        return self.__saldo

     # Metodo visualizza saldo
    def visualizza_saldo(self) -> float:
        return self.__saldo 
    
    # Getter del titolare
    def get_titolare(self) -> str:
        return self.__titolare
    
    # Setter del titolare con validazione di stringa non vuota
    def set_titolare(self, nome: str) -> None:
        nome_str = str(nome).strip()  # converto in stringa e rimuovo spazi
        if nome_str:                  # se non è vuoto
            self.__titolare = nome_str
            
    # Rappresentazione leggibile dell'oggetto
    def __str__(self) -> str:
        return f"ContoBancario(titolare={self.__titolare}, saldo={self.__saldo:.2f} €)"

    # __repr__ per debug → riusa __str__
    def __repr__(self) -> str:
        return self.__str__()
