# --- Import delle classi ---
from sottoclassi import *
from gestoreflotta import GestoreFlotta

def main():
    # Creazione del gestore
    flotta = GestoreFlotta()

    # Creazione di alcuni veicoli
    camion1 = Camion("AB123CD", 10000, 4)
    furgone1 = Furgone("EF456GH", 2000, "diesel")
    motocarro1 = Motocarro("IJ789KL", 800, 5)

    # Aggiunta alla flotta
    flotta.aggiungi_veicolo(camion1)
    flotta.aggiungi_veicolo(furgone1)
    flotta.aggiungi_veicolo(motocarro1)

    # Operazioni di carico
    camion1.carica(3000)
    furgone1.carica(500)
    motocarro1.carica(200)

    # Stampa situazione flotta
    print("\n--- Veicoli in flotta ---")
    flotta.stampa_veicoli()

    # Calcolo manutenzione totale
    totale = flotta.costo_totale_manutenzione()
    print(f"\nCosto totale manutenzione annuale: {totale} €")

    # Scarico di un veicolo
    print("\n--- Scarico camion ---")
    camion1.scarica()

    # Rimozione di un veicolo
    print("\n--- Rimozione furgone ---")
    flotta.rimuovi_veicolo("EF456GH")

    # Stampa finale
    print("\n--- Flotta aggiornata ---")
    flotta.stampa_veicoli()

if __name__ == "__main__":
    main()
