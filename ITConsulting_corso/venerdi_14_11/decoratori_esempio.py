# ==========================================================
# DECORATORI
# ==========================================================
# esempio 1
def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione di una funzione")
        funzione()
        print("Dopo dell'esecuzione di una funzione")
    return wrapper 

@decoratore 
def saluta():
    print("Ciao!")
    
saluta()

# esempio 2
print(" =========== ESEMPIO 2 ===========")
def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato 
    return wrapper 

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a+b 

print("risultato è", somma(3, 4))