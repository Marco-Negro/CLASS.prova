class Persona: # class è la direttiva. python capisce quale nome gli dò..(Class ha sempre nome proprio con Maiuscola iniziale)
    def __init__(self, nome, eta=None): # self serve per accedere agli attributi all' interno dell'oggetto.
        # none si usa se vogliamo mettere NESSUN VALORE di default"
        self.nome = nome    # self --> chiama se stesso in quanto oggetto
        self.eta = eta

    def saluta(self):
        print(f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni.")#self.nome <-- ANCHE NEL COSTRUCTOR PERCHè CREA L'OGGETTO

p1 = Persona("Marco",32)  # la classe la puoi mettere anche all'interno non per forza all'esterno della classe
p1.saluta()
p1.eta = 99     
p1.saluta()
# print(A SCHERMO AVREMO:)
# Ciao, mi chiamo Marco e ho 32 anni.
# Ciao, mi chiamo Marco e ho 99 anni.             stiamo modificando il valore dell'età.
#---------------------------------------------------------------------------------
