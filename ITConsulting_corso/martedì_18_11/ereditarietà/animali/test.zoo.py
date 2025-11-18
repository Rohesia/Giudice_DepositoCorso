from specie import Leone, Giraffa, Pinguino, Elefante

# Creiamo gli animali
leone1 = Leone("Simba", 5, velocita=60)
giraffa1 = Giraffa("Cleo", 7, attenzione=8)
pinguino1 = Pinguino("Pingu", 3, cammino=5)
elefante1 = Elefante("Dumbo", 9)  

# Test del Leone
print("--- Leone ---")
leone1.fai_suono()
leone1.caccia()

# Test della Giraffa
print("\n--- Giraffa ---")
giraffa1.fai_suono()
giraffa1.osserva()

# Test del Pinguino
print("\n--- Pinguino ---")
pinguino1.fai_suono()
pinguino1.cammina()

# Test dell'Elefante 
print("\n--- Elefante ---")
elefante1.fai_suono()
print(elefante1.nome, elefante1.eta)
