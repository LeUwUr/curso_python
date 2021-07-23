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

class furgoneta(vehiculos):

    def carga(self, cargar):
        self.cargado=cargar

        if(self.cargado):
            return "La furgoneta esta cargada"

        else:
            return "La furgoneta no esta cargada"

class VElectricos():
    def __init__(self):
        self.autonomia=100

    def cargarEnergia(self):
        self.cargando=True
        
        

class moto(vehiculos):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

    def estado(self):
        print("MARCA: ", self.marca, "\nMODELO: ", self.modelo, "\nEN MARCHA: ",
            self.enmarcha, "\nACELERANDO: ", self.acelera, "\nFRENADO: ", self.frena, "\n", self.hcaballito)

miMoto=moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

print("*+*+*+*+ SIGUIENTE VEHICULO *+*+*+*+")

miFurgoneta=furgoneta("Renault", "KAGOO")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class bicicletaElectrica(VElectricos,vehiculos):
    pass

miBici=bicicletaElectrica()