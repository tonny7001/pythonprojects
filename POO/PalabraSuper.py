# Clase padre
class Rectangulo:  
    # Método constructor
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

# Clases hijas        
class Cuadrado(Rectangulo):
    def __init__(self, alto, ancho):
        super().__init__(alto, ancho)
       
    def area(self):
        return self.alto * self.ancho

class Cubo(Rectangulo):
    def __init__(self, alto, ancho, largo):
        super().__init__(alto, ancho)
        self.largo = largo
        
    def volumen(self):
        return self.alto * self.ancho * self.largo

# Creación de los objetos
cuadrado = Cuadrado(3, 3) 
cuadrado1 = Cuadrado(2, 6)
cubo = Cubo(3, 3, 3)
          
print(f"El área de {cuadrado.alto} y {cuadrado.ancho} es: {cuadrado.area()}")       
print(f"El área de {cuadrado1.alto} y {cuadrado1.ancho} es: {cuadrado1.area()}")       
print(f"El volumen de {cubo.alto}, {cubo.ancho} y {cubo.largo} es: {cubo.volumen()}")

         
        