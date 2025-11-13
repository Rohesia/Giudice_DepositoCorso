# ==========================================================
# USO di break
# ==========================================================

numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    if numero == 3:
        break
    print(numero)
    
# ==========================================================
# USO di continue
# ==========================================================

numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    if numero == 3:
        continue 
    print(numero)
    
# ==========================================================
# USO di pass
# ==========================================================

for i in range(5):
    if i == 3:
        pass
    print(i)
    
# ==========================================================
# USO di *
# ==========================================================

numeri = [*range(1, 11)]
print(numeri)
    
# ==========================================================
# ESEMPIO con break e continue
# ==========================================================

prenotazioni = ["Luca", "vuoto", "Anna", "Marco", "chiuso", "Paolo"]

for nome in prenotazioni:
    if nome == "chiuso":
        print("Cinema chiuso. Interrompe il controllo")
        break 
    
    if nome == "vuoto":
        print("posto libero")
        continue 
    
    if nome == "Marco":
        pass 
    
    print(f"Posto occupato da: {nome}")

print("Controllo terminato.")
    