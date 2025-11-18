from ruoli import Giocatore, Allenatore, Assistente

# Creazione dei membri della squadra
giocatore1 = Giocatore("Luca", 24, ruolo="Attaccante", numero_maglia=9)
allenatore1 = Allenatore("Marco", 50, anni_esperienza=20)
assistente1 = Assistente("Sara", 35, specializzazione="Fisioterapista")

# Test dei membri
print("--- Giocatore ---")
giocatore1.descrivi() #oveeride
giocatore1.gioca_partita()

print("\n--- Allenatore ---")
allenatore1.descrivi() #override
allenatore1.dirigi_allenamento()

print("\n--- Assistente ---")
assistente1.descrivi() #classe figlia
assistente1.supporta_team()


print("\n--- Simulazione Partita ---")
allenatore1.dirigi_allenamento()
giocatore1.gioca_partita()
assistente1.supporta_team()
allenatore1.incoraggia()
giocatore1.segna_goal()
