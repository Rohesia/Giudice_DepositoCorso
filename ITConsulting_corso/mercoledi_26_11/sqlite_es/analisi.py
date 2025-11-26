import numpy as np 

def posizione_misura(data):
    return {
        "min": np.min(data, axis=0),
        "max": np.max(data, axis=0),
        "mean": np.mean(data, axis=0),
        "median": np.median(data, axis=0),
        "std": np.std(data, axis=0)
    }

    
def interpretazione(stats, column_names):
    testo = "\n=== Interpretazione statistica ===\n"

    for i, col in enumerate(column_names):
        testo += f"\n Variabile: {col}\n"
        testo += f" - Minimo: {stats['min'][i]}\n"
        testo += f" - Massimo: {stats['max'][i]}\n"
        testo += f" - Media: {stats['mean'][i]}\n"
        testo += f" - Mediana: {stats['median'][i]}\n"
        testo += f" - Deviazione standard: {stats['std'][i]}\n"

        testo += (
            "\nInterpretazione:\n"
            "La media suggerisce il valore tipico della variabile, mentre la mediana "
            "indica il valore centrale non influenzato dagli outlier. "
            "Se media e mediana sono molto diverse, significa che la distribuzione "
            "è asimmetrica. La deviazione standard ci dice quanto i valori "
            "sono dispersi rispetto alla media.\n"
        )

    return testo
