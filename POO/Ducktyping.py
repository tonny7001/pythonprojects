# Clases

class Pato:
    def caminar(self):
        print('Este pato está caminando.')
        
    def hablar(self):
        print('Este pato está haciendo cuac.')

class Gallina:
    def caminar(self):
        print('La gallina está caminando.')
        
    def hablar(self):
        print('Esta gallina está cacareando.')    
        
class Persona:
    def atrapar(self, pato):
        pato.caminar()
        pato.hablar()
        print('¡Lo atrapaste!')

# Creación de instancias
pato = Pato()
gallina = Gallina()
persona = Persona()

# Usar la función atrapar
persona.atrapar(pato)


#nota los metodos de las clases tienen que ser iguales asi el mensaje sea diferente 
