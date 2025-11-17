# ==========================================================
# CLASSE RISTORANTE
# ==========================================================
def separatore(funzione):
    def wrapper(*args, **kwargs):
        print("\n" + "="*40)  
        risultato = funzione(*args, **kwargs)
        print("="*40 + "\n")  
        return risultato
    return wrapper

class Ristorante:
    def __init__(self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False
        self.menu = {}
        
    # metodo per descrivere il ristorante 
    @separatore
    def descrivi_ristorante(self):
        print(f"Il ristorante {self.nome} offre cucina {self.tipo_cucina}")
    
    # metodo per controllare lo stato di apertura
    @separatore
    def stato_apertura(self):
        if self.aperto:
            print(f"Il ristorante {self.nome} in questo momento è aperto")
        else: 
            print(f"Il ristorante {self.nome} in questo momento è chiuso")
        
    # apertura ristorante
    @separatore
    def apri_ristorante(self):
        if self.aperto == True:
            print(f"Il ristorante {self.nome} è aperto")
    
    # chiusura del ristorante
    @separatore
    def chiudi_ristorante(self):
        if self.aperto == False: 
            print(f"Il ristorante {self.nome} è chiuso")
    
    # aggiunta di piatti 
    @separatore
    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo 
        print(f"Abbiamo aggiunto al menu il {piatto} al prezzo di {prezzo}€")
    
    # rimozione 
    @separatore
    def togli_dal_menu(self, piatto):
        rimosso = self.menu.pop(piatto, None)
        if rimosso is not None:
            print(f"{piatto} rimosso dal menu.")
        else:
            print(f"{piatto} non è presente nel menu.")
    
    # stampa del menu 
    @separatore
    def stampa_menu(self):
        print("Menu del ristorante:")
        if self.menu:
            for piatto, prezzo in self.menu.items():
                print(f"{piatto}: {prezzo}€")
        else:
            print("Menu vuoto")