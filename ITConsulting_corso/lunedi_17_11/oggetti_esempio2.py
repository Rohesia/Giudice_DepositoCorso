# ==========================================================
# CLASSE FIORE
# ==========================================================

# Classe fiore
class Fiore:
    specie_generica = "Pianta"  # attributo di classe comune a tutti i fiori

    def __init__(self, nome, colore):
        self.nome = nome      
        self.colore = colore  

    # metodo per stampare informazioni sul fiore
    def stampa_info(self):
        print("Il fiore si chiama", self.nome, "ed è di colore", self.colore)

    # metodo speciale 
    def __str__(self):
        return f"Fiore(nome={self.nome}, colore={self.colore})"


# Creazione delle istanze (oggetti)
fiore1 = Fiore("Rosa", "rossa")
fiore2 = Fiore("Tulipano", "giallo")

# Uso dei metodi
fiore1.stampa_info()
fiore2.stampa_info()

# Stampa 
print(fiore1)
print(fiore2)
