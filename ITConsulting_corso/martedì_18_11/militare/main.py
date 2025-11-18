from controllomilitare import *
from classiderivate import *

print("\n=== SISTEMA DI CONTROLLO MILITARE ===\n")

# Creo il centro di controllo
centro = ControlloMilitare()

# Creo le unità militari in una lista
unita = [
    Fanteria("Fanteria Alfa", 50),
    Artiglieria("Artiglieria Bravo", 20),
    Cavalleria("Cavalleria Delta", 30),
    SupportoLogistico("Supporto Eco", 10),
    Ricognizione("Ricognizione Zeta", 8)
]

# Registro tutte le unità
for u in unita:
    centro.registra_unita(u)

print()

# Mostro tutte le unità registrate
centro.mostra_unita()

print("\n--- Azioni ---")
# Chiamo il metodo speciale di ciascuna unità
# Ogni classe definisce questo metodo
for u in unita:
    u.azione_speciale()   

print("\n--- Dettagli singola unità ---")
centro.dettagli_unita("Cavalleria Delta")

print("\n--- Movimento ---")
# Eseguiamo azioni generiche
for u in unita:
    u.muovi()
    u.attacca()
    u.ritira()

print("\n=== FINE ===\n")
