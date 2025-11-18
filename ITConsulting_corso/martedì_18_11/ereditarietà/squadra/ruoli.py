from membrosquadra import MembroSquadra
import random
# ------------------------------------------------
# Classe Giocatore
# ------------------------------------------------
class Giocatore(MembroSquadra):
    def __init__(self, nome: str, eta: int, ruolo: str, numero_maglia: int):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        self.goal = 0
        
    # il giocatore riponde ai comandi imposti dall'allenatore    
    def rispondi_comando(self, comando: str):
        print(f"{self.nome} risponde: eseguo '{comando}!'")
    # viene eseguita un'azione random tra quelli presenti nella lista
    def gioca_partita(self):
        azione = random.choice(["tira in porta", "passa la palla", "dribbla un avversario"])
        print(f"{self.nome} {azione} come {self.ruolo}!")
    # viene tenuto il conteggio dei goal fatti -> è un normale contatore
    def segna_goal(self):
        self.goal += 1
        print(f"{self.nome} ha segnato! Goal totali: {self.goal}")
# ------------------------------------------------
# Classe Allenatore
# ------------------------------------------------
class Allenatore(MembroSquadra):
    def __init__(self, nome: str, eta: int, anni_esperienza: int):
        super().__init__(nome, eta)
        self.anni_esperienza = anni_esperienza
        
    # allenatore dà un comando al giocatore
    def dai_comando(self, comando: str, giocatore):
        print(f"{self.nome} dice a {giocatore.nome}: '{comando}'")
        giocatore.rispondi_comando(comando)

    # stampa una frase random tra quelli nella lista
    def incoraggia(self):
        frasi = ["Forza squadra!", "Non mollate!", "Oggi vinciamo!"]
        print(f"{self.nome} dice: {random.choice(frasi)}")
        
    
    def dirigi_allenamento(self):
        print(f"{self.nome} dirige l'allenamento della squadra.")

# ------------------------------------------------
# Classe Assistente
# ------------------------------------------------
class Assistente(MembroSquadra):
    def __init__(self, nome: str, eta: int, specializzazione: str):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione

    def descrivi(self):
        print(f"{self.nome}, {self.eta} anni, assistente con specializzazione in {self.specializzazione}.")

    def supporta_team(self):
        print(f"{self.nome} supporta il team in quanto competente in {self.specializzazione}.")
