import numpy as np

class GestoreMatrice:
    def __init__(self):
        # Inizializza la matrice e il file di salvataggio
        self._matrice = None
        self.file = "matrice.txt"
        
    def _check_matrice(self):
        # Controlla che la matrice sia stata creata
        if self._matrice is None:
            print("Nessuna matrice creata.")
            return False
        return True

    def salva(self, testo):
        # Salva il testo su file
        with open(self.file, "a") as f:
            f.write(testo + "\n")
        print("Risultato salvato su file.")

    def crea_matrice(self):
        # Crea una matrice 2D casuale con dimensioni da input
        print("\n=== CREAZIONE NUOVA MATRICE ===")
        r = int(input("Inserisci il numero di righe: "))
        c = int(input("Inserisci il numero di colonne: "))

        if r <= 0 or c <= 0:
            print("Le dimensioni devono essere positive.")
            return

        self._matrice = np.random.randint(0, 101, size=(r, c))
        print("\nMatrice generata:")
        print(self._matrice)
        self.salva(f"Creazione matrice ({r}x{c}):\n{self._matrice}")

    def sotto_matrice(self):
        # Estrae la sotto-matrice centrale
        if not self._check_matrice():
            return

        r, c = self._matrice.shape
        ri, rf = r // 4, r - r // 4
        ci, cf = c // 4, c - c // 4

        sub = self._matrice[ri:rf, ci:cf]
        print("\nSotto-matrice centrale:")
        print(sub)
        self.salva(f"Sotto-matrice centrale:\n{sub}")

    def trasponi(self):
        # Trasposta della matrice 
        if not self._check_matrice():
            return

        mat_trasp = self._matrice.T  
        print("\nMatrice trasposta:")
        print(mat_trasp)
        self.salva(f"Matrice trasposta:\n{mat_trasp}")

    def somma(self):
        # Calcola la somma di tutti gli elementi
        if not self._check_matrice():
            return

        totale = np.sum(self._matrice)
        print(f"\nSomma di tutti gli elementi: {totale}")
        self.salva(f"Somma elementi: {totale}")

    def media(self):
        # Calcola la media di tutti gli elementi
        if not self._check_matrice():
            return

        media_val = np.mean(self._matrice)
        print(f"\nMedia degli elementi: {media_val:.2f}")
        self.salva(f"Media elementi: {media_val:.2f}")

    def moltiplicazione_elementwise(self):
        # Moltiplicazione element-wise con un'altra matrice delle stesse dimensioni
        if not self._check_matrice():
            return

        r, c = self._matrice.shape
        print(f"\n=== CREAZIONE SECONDA MATRICE ({r}x{c}) PER MOLTIPLICAZIONE ===")
        seconda_matrice = np.random.randint(0, 101, size=(r, c))
        print("Seconda matrice generata:")
        print(seconda_matrice)

        risultato = np.multiply(self._matrice, seconda_matrice)
        print("\nRisultato moltiplicazione element-wise:")
        print(risultato)
        self.salva(f"Moltiplicazione element-wise:\n{risultato}")
        
    def determinante(self):
        if not self._check_matrice():
            return None
        
        r, c = self._matrice.shape
        if r != c:
            print("\nLa matrice non è quadrata, impossibile calcolare il determinante.")
            return None

        det = np.linalg.det(self._matrice)
        print(f"\nDeterminante della matrice: {det:.2f}")
        self.salva(f"Determinante della matrice: {det:.2f}")

        return det

    
    def matrice_inversa(self):
        if not self._check_matrice():
            return

        det = self.determinante()  

        if det is None:
            return

        if det == 0:
            print("\nLa matrice non è invertibile perché il determinante è 0.")
            return

        inv = np.linalg.inv(self._matrice)
        print("\nMatrice inversa:")
        print(inv)
        self.salva(f"Matrice inversa:\n{inv}")