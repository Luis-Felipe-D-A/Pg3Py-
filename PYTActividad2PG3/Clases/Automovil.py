from Clases.Vehiculo import *

class Automovil(Vehiculo):
    def __init__(self, FechaDEfabricacion, VIN_chasis, VINMotor, marca, modelo, precio):
        super().__init__(FechaDEfabricacion, VIN_chasis, VINMotor)
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    
    def obtener_marca(self):
        return self.marca

    def obtener_modelo(self):
        return self.modelo

    def obtener_precio(self):
        return self.precio

    def imprimir(self):
        print(f"Fecha de Fabricación: {self.obtener_FechaDEfabricacion()}")
        print(f"VIN del Chasis: {self.obtener_VIN_chasis()}")
        print(f"VIN del Motor: {self.obtener_VINMotor()}")
        print(f"Marca: {self.obtener_marca()}")
        print(f"Modelo: {self.obtener_modelo()}")
        print(f"Precio: ${self.obtener_precio():,.2f}")
