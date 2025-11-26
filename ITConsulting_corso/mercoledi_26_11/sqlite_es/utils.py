import csv 
import numpy as np 


# caricamento del file csv
def carica_csv(path):
    with open(path, 'r', encoding="utf-8") as f:   # <-- corretto
        reader = csv.reader(f)
        headers = next(reader)
        righe = [row for row in reader]
        
    # conversione in numeri a virgola mobile    
    dati = np.array(righe, dtype=float)
    
    return headers, dati


# rimuovere righe 
def rimuovi_nan(dati):
    # Creo una lista di valori True/False per ogni riga:
    # True se la riga NON contiene NaN, False se contiene almeno un NaN
    righe_valide = []
    for riga in dati:
        if not np.isnan(riga).any():  # se non ci sono NaN nella riga
            righe_valide.append(True)
        else:
            righe_valide.append(False)

    # Seleziono solo le righe valide
    dati_puliti = dati[righe_valide]
    return dati_puliti


# rimuovere outlier 
def rimuovi_outlier(dati, limite=3):
    
    media = np.mean(dati, axis=0)          # calcolo la media di ogni colonna
    deviazione = np.std(dati, axis=0)      # calcolo la deviazione standard di ogni colonna
    
    righe_normali = []
    for riga in dati:
        riga_valida = True
        for i in range(len(riga)):
            # se un valore è troppo lontano dalla media, escludo la riga
            if abs(riga[i] - media[i]) > limite * deviazione[i]:
                riga_valida = False
        if riga_valida:
            righe_normali.append(riga)
    
    return np.array(righe_normali)
    
