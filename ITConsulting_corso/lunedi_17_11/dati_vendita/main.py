# ==========================================================
# MAIN
# ==========================================================
from dati_vendita import *

vendite = []

for i in range(3):
    numero = input(f"Inserisci l'importo delle vendite del giorno {i+1}: ")
    # conversione in intero
    vendite.append(int(numero))

# creo oggetto analizzatore
analisi = AnalisiVendite(vendite)

# stampa
print("\n--- Risultati Generali ---")
print("Dati di vendita inseriti:", vendite)
print("Totale vendite:", analisi.totale())
print("Media vendite:", analisi.media())

sopra_media = analisi.sopra_media()
print("\n--- Giorni con vendite sopra la media ---")
if len(sopra_media) == 0:
    print("Non ci sono giorni con vendite sopra la media.")
else:
    for giorno, valore in sopra_media:
        print(f"Giorno {giorno}: vendita = {valore}")

print("\nFine analisi dati.")
