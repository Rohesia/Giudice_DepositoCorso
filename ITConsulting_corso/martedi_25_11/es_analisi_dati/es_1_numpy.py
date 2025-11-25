import numpy as np
import os
from datetime import datetime

def genera_array(n=50):
    # generazione array: uno lineare e uno causale
    arr_lin = np.linspace(0, 10, n)
    arr_rand = np.random.random(n)
    return arr_lin, arr_rand

def analizza_array(arr_lin, arr_rand):
    #Calcola somma, totale e somma condizionata
    arr_sum = arr_lin + arr_rand
    risultati = {
        "array_somma": arr_sum,
        "totale": arr_sum.sum(),
        "mag5": arr_sum[arr_sum > 5].sum()
    }
    return risultati

def stampa_risultati(arr_lin, arr_rand, risultati):
    print("\n=== RISULTATI ESECUZIONE ===")
    print("Array linspace:", arr_lin)
    print("\nArray random:", arr_rand)
    print("\nArray somma:", risultati["array_somma"])
    print(f"\nSomma totale: {risultati['totale']}")
    print(f"Somma degli elementi > 5: {risultati['mag5']}")

def salva_su_file(arr_lin, arr_rand, risultati, file_txt="numpy_es.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mode = "a"
    if os.path.exists(file_txt):
        scelta = input("\nIl file esiste già. Sovrascrivere? (s/n): ").strip().lower()
        if scelta == "s":
            mode = "w"

    with open(file_txt, mode) as f:
        f.write(f"\n=== Nuova esecuzione ({timestamp}) ===\n")
        f.write("Array linspace:\n" + str(arr_lin) + "\n\n")
        f.write("Array random:\n" + str(arr_rand) + "\n\n")
        f.write("Array somma:\n" + str(risultati["array_somma"]) + "\n\n")
        f.write(f"Somma totale: {risultati['totale']}\n")
        f.write(f"Somma elementi > 5: {risultati['mag5']}\n")

    print(f"\n Dati salvati in: {file_txt}")

def main():
    print("\n=== PROGRAMMA NUMPY ===")
    while True:
        arr_lin, arr_rand = genera_array()
        risultati = analizza_array(arr_lin, arr_rand)

        stampa_risultati(arr_lin, arr_rand, risultati)
        salva_su_file(arr_lin, arr_rand, risultati)

        if input("\nVuoi ripetere? (s/n): ").strip().lower() != "s":
            print("\nProgramma terminato")
            break

if __name__ == "__main__":
    main()
