# esempio 1
class Computer:
    def __init__(self):
        self.__processore = "Intel i5"
        
    def get_processore(self):
        return self.__processore 
    
    def set_processore(self, processore):
        self.__processore = processore
        
pc = Computer() 
print(pc.get_processore()) 

# accede all'attributo privato tramile il getter
pc.set_processore("AMD Ryzen 5")

# modifica l'attributo privato tramite il set
print(pc.get_processore())

# esempio 2 
# variabile globale 
numero = 10 

def funzione_esterna():
    # variabile locale nella funzione esterna 
    numero = 5
    print("variabile locale nella funzione esterna (local): ", numero)
    
    def funzione_interna():
        # uso di non local per modificare la variabile locale della funzione esterna 
        nonlocal numero 
        numero = 3 
        print("numero dento la funzione interna (nonlocal):", numero)
        
    funzione_interna()
    
print("numero nel main (globale):", numero)
funzione_esterna() 
print("numero nel main dopo chiamata (globale non cambiato): ", numero)

# esempio 3 
class Persona:
    def __init__(self, nome):
        self.nome = nome

    # Metodo pubblico
    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome}")
        # Chiamo il metodo privato dall’interno della classe
        self.__messaggio_privato()

    # Metodo privato
    def __messaggio_privato(self):
        print("Questo è un messaggio privato!")


# Creazione dell'oggetto
persona1 = Persona("Ludovica")

# Chiamare il metodo pubblico
persona1.saluta()  

# Tentativo di chiamare il metodo privato dall'esterno (non consigliato)
# persona1.__messaggio_privato()  # Genera errore


#esempio 4 
class ClasseBase:
    def __init__(self):
        self._variabile_protetta = " sono protetta"
        
class SottoClasse(ClasseBase):
    def __init__(self):
        super().__init__()
        print(self._variabile_protetta)
        
obj = SottoClasse()
# accesso fuori classe (non consigliato, ma possibile)
print(obj._variabile_protetta)