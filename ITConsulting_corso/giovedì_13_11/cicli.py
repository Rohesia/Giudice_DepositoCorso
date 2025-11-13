# ciclo matematico 
 
conteggio = 0 

while conteggio < 5:
    print(conteggio)
    conteggio += 1
    
# ciclo booleano
controllor = True 
while controllor:
    print(controllor)
    scelta = input("vuoi continuare?")
    if scelta.lower == "no":
        controllor = False
    else: 
        print("stai continuando")
    break
        
# ciclo for 
numeri = [ 1, 2, 3, 4, 5]

for numero in numeri:
    print(numero)
    
# range 
for i in range(5):
    print(i)
    
# range con start e stop 
for i in range(2, 8):
    print(i)

# range con step 
for i in range(1, 10, 2):
    print(i)