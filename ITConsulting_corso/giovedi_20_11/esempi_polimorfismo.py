class Assistant:
    def ripeti(self, messaggio):
        return "Implemento il metodo nella sottoclasse."


class Assistente1(Assistant):
    def ripeti(self, messaggio):
        return f"Ecco la tua risposta riguardo: '{messaggio}'"


class Assistente2(Assistant):
    def ripeti(self, messaggio):
        return f"Uffa! Ancora un'altra domanda sul '{messaggio}'"


class Assistente3(Assistant):
    def ripeti(self, messaggio):
        return f"[Analisi richiesta: {messaggio}] Output generato con parametri avanzati"


class Assistente4(Assistant):
    def ripeti(self, messaggio):
        return "Ok."


def chiedi(bot: Assistant, domanda: str):
    print(bot.ripeti(domanda))


bots = [
    Assistente1(),
    Assistente2(),
    Assistente3(),
    Assistente4()
]

for b in bots:
    chiedi(b, "come funziona il polimorfismo?")

# esempio 2 
class Stampa:
    def mostra(self, a = None, b = None):
        if a is not None and b is not None:
            print(a + b)
        elif a is not None: 
            print(a)
        else: 
            print("niente da mostrare")
            
# duck type 
# esempio 1
class Polpo:
    def emetti_suono(self):
        return "Squish-squish!"

class Delfino:
    def emetti_suono(self):
        return "Click-click!"

class Balena:
    def emetti_suono(self):
        return "Woooaaa!"

# Funzione che sfrutta duck typing
def ascolta_suono(creatura):
    print(creatura.emetti_suono())

# Lista di creature diverse
acquario = [Polpo(), Delfino(), Balena()]

for c in acquario:
    ascolta_suono(c)


# esempio 2
class Cane:
    def parla(self):
        return "Bau!"
    
class Gatto:
    def parla(self):
        return "Miao!"
    
def fai_parlare(animale):
    # non importa il tipo di animale
    print(animale.parla())
    
cane = Cane() 
gatto = Gatto() 

fai_parlare(cane)
fai_parlare(gatto)

# esempio 3 
class Cerchio:
    def disegna(self):
        print("disegna un cerchio")
        
class Rettangolo:
    def disegna(self):
        print("Disegna un rettangolo")

def disegna_figura(figura):
    # basta che figura abbia disegna
    figura.disegna()
    
figure = [Cerchio(), Rettangolo()]

for figura in figure:
    disegna_figura(figura)