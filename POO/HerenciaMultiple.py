class Presa:
    def huir(self):
        print("Este animal esta huyendo")
    
class Depredador:
    def cazar(self):
        print("animal esta cazando")

class Conejo(Presa):
    pass        
        
class Halcon(Depredador):
    pass       

class Pez(Presa, Depredador):
    pass


conejo = Conejo()

halcon= Halcon()

pez = Pez()

pez.cazar
