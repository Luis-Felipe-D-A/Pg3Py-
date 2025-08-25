class Vehiculo:
    def __init__(self, FechaDEfabricacion, VIN_chasis, VINMotor):
        self.FechaDEfabricacion = FechaDEfabricacion
        self.VIN_chasis = VIN_chasis
        self.VINMotor = VINMotor

    def obtener_FechaDEfabricacion(self):
        return self.FechaDEfabricacion

    def obtener_VIN_chasis(self):
        return self.VIN_chasis

    def obtener_VINMotor(self):
        return self.VINMotor

    
