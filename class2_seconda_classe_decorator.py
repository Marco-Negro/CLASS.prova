# esempi (non funziona, da mettere mano)
class Persona: 
    def __init__(self, nome, eta): # serve sempre per creare l'oggetto base.
        
        self.nome = nome    
        self.eta = eta

# UTILIZZARE IL DECORATORE è PROFESSIONALE PIù di __init__
    @classmethod
    def solo_nome(cls, nome):
        return cls(nome, 0)

p1 = Persona("Marco",32) 

p1.eta = 99     


print(Persona.quante_persone())