# Para crear un objeto primero se crea la clase

# 1. Crear la clase 
class Carro: 
    
    ruedas=4
    # 2. Crear el método constructor    
    def __init__(self, marca, modelo, ano, color):       
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color

    # Crear funciones
    def encendido(self): 
        print("El auto está encendido")  
        
    def apagado(self):
        print("El auto está apagado")
