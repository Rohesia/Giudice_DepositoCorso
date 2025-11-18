class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca 
        self.modello = modello 
        
    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")
        
        

class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
        
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")
        
        
class AutomobileSportiva(Veicolo, DotazioniSpeciali):
    def __init__(self, marca, modello, dotazioni, cavalli):
        Veicolo.__init__(self, marca, modello)
        # alternativa a super per ereditarietà multipla 
        DotazioniSpeciali.__init__(self, dotazioni)
        self.cavalli = cavalli 
        
    def mostra_informazioni(self):
        super().mostra_informazioni()
        # chiamiamo la superclasse 
        print(f"potenza: {self.cavalli} CV")
        self.mostra_dotazioni()
        # chiamiamo i metodi delle superclassi
        
    