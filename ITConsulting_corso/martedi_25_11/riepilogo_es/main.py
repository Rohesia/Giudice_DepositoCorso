from matrice import GestoreMatrice

def menu(gestore):
    while True:
        print("\n=== MENU GESTORE MATRICE ===")
        print("1. Crea matrice")
        print("2. Sotto-matrice centrale")
        print("3. Trasponi matrice")
        print("4. Somma elementi")
        print("5. Media elementi")
        print("6. Moltiplicazione element-wise")
        print("7. Determinante matrice")
        print("8. Matrice inversa")
        print("9. Esci")
        
        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            gestore.crea_matrice()
        elif scelta == "2":
            gestore.sotto_matrice()
        elif scelta == "3":
            gestore.trasponi()
        elif scelta == "4":
            gestore.somma()
        elif scelta == "5":
            gestore.media()
        elif scelta == "6":
            gestore.moltiplicazione_elementwise()
        elif scelta == "7":
            gestore.determinante()
        elif scelta == "8":
            gestore.matrice_inversa()
        elif scelta == "9":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida, riprova.")


if __name__ == "__main__":
    gestore = GestoreMatrice()
    menu(gestore)
