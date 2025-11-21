file = open("ciao.txt", "r")



contenuto = file.read() 
riga = file.readline()
file.write("questo è un esempio di scrittura su file")


with open("ciao.txt", "w") as file:
    file.write("questo è un esempio di scrittura su file")
