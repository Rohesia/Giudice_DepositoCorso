from prodotto import * 
from fabbrica import * 

# creazione prodotti
# Elettronica
elettronica1 = Elettronica("Laptop", 500, 800, 2)
elettronica2 = Elettronica("Lampada LED", 20, 45, 1)

# Abbigliamento
abbigliamento1 = Abbigliamento("Jeans", 30, 60, "Denim")
abbigliamento2 = Abbigliamento("T-shirt", 10, 25, "Cotone")

# creazione fabbrica
fabbrica = Fabbrica("Technology and Fashion")

# aggiungere prodotti
fabbrica.aggiungi_prodotto(elettronica1, 10)
fabbrica.aggiungi_prodotto(abbigliamento1, 50)
fabbrica.aggiungi_prodotto(elettronica2, 10)
fabbrica.aggiungi_prodotto(abbigliamento2, 50)

# vendere prodotti
fabbrica.vendi_prodotto(elettronica1, 3)
fabbrica.vendi_prodotto(abbigliamento1, 20)  # correggiamo passando l'oggetto giusto

# resi
fabbrica.resi_prodotto(elettronica1, 1)

# mostra inventario
fabbrica.mostra_inventario()
