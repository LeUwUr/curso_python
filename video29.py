class vehiculos():

    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("MARCA: ", self.marca, "\nMODELO: ", self.modelo, "\nEN MARCHA: ",
            self.enmarcha, "\nACELERANDO: ", self.acelera, "\nFRENADO: ", self.frena)

class moto(vehiculos):
    pass

miMoto=moto("Honda", "CBR")

miMoto.estado()