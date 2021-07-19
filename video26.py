class Coche():
    largoChasis=250
    anchoChasis=12
    ruedas=4
    enmarcha=False

    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if(self.enmarcha):
            return "El coche esta en marcha."

        else:
            return "El coche esta parado."

toyota=Coche()

print("El largo del coche es:",toyota.largoChasis)
print("El coche tiene:",toyota.ruedas,"ruedas")

toyota.arrancar()

print(toyota.estado())