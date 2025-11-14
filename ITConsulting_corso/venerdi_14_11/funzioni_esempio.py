# ==========================================================
# FUNZIONI
# ==========================================================

#Esempio 1 
def saluta(nome):
    print("Ciao, ", nome)
    print("Benvenuto nel nostro programma!")
    
# Esempio 2 
def somma(a, b):
    risultato = a + b
    print("La somma è: ", risultato)
    
# richiamo della funzione
saluta("Alice")
somma(5, 3)
    
    
# valore di ritorno 
def quadrato(numero):
    return numero * numero 

risultato = quadrato(4)
print(risultato)

# ==========================================================
# FUNZIONI - ESEMPIO SEMPLICE
# ==========================================================
print("==========================================================")
print(" ======== ESERCIZIO ESEMPIO ==========")
print("==========================================================")

# Funzione 1: saluto
def saluto(nome):
    print(f"Ciao {nome}! Benvenuto nella cucina\n")

# Funzione 2: prepara un piatto
def prepara_piatto(piatto):
    print(f"Il tuo piatto di {piatto} è pronto!\n")

# Funzione 3: conta piatti preparati
def conta_piatto(numero_piatti):
    print(f"Sono stati preparati {numero_piatti} piatti oggi.\n")

# =========================
# RICHIAMO DELLE FUNZIONI
# =========================
saluto("Alice")

prepara_piatto("Pizza")
prepara_piatto("Tiramisù")

conta_piatto(2)
