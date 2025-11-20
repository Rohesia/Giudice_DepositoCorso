from ITConsulting_corso.giovedi_20_11.pagameti_esercizio.gestore_pagamenti import GestorePagamenti
from sottoclassi import *
class GestorePagamenti:
    def __init__(self, metodo_pagamento: MetodoPagamento):
        self.__metodo_pagamento: MetodoPagamento = metodo_pagamento 
        
    def paga(self, importo: float) -> bool: 
        return self.__metodo_pagamento.effettua_pagamento(importo)
    
    def cambia_metodo(self, nuovo_metodo: MetodoPagamento) -> None:
        self.__metodo_pagamento = nuovo_metodo 
        
        
    def get_metodo_pagamento(self) -> MetodoPagamento:
        return self.__metodo_pagamento