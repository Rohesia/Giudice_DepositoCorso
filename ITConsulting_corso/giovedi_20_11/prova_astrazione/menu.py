
# --- Classe MenuItem ---
class MenuItem:
    """Rappresenta una singola voce di menu con un'azione associata."""

    def __init__(self, nome: str, descrizione: str, azione):
        self.nome = nome
        self.descrizione = descrizione
        self.azione = azione  

    def esegui(self):
        """Esegue l'azione associata alla voce di menu."""
        self.azione()

    def __str__(self):
        return f"{self.nome}: {self.descrizione}"


# --- Classe Menu ---
class Menu:
    """Gestore interattivo di un menu testuale."""

    def __init__(self, titolo: str, voci=None):
        self.titolo = titolo
        self.voci = voci if voci is not None else []

    def aggiungi_voce(self, voce: MenuItem):
        self.voci.append(voce)

    def mostra(self):
        print(f"\n=== {self.titolo} ===")
        i = 1
        for voce in self.voci:
            print(f"{i}. {voce}")
            i += 1
        print(f"{i}. Esci")
        
    def seleziona(self):
        while True:
            self.mostra()
            scelta = input("Seleziona un'opzione: ").strip()
            if not scelta.isdigit():
                print("Input non valido. Inserisci un numero.")
                continue
            indice = int(scelta)
            
            if indice == len(self.voci) + 1:
                print("Uscita dal menu.")
                break
            elif 1 <= indice <= len(self.voci):
                self.voci[indice - 1].esegui()
            else:
                print("Opzione non valida. Riprova.")

