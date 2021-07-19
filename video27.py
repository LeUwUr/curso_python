class Coche():

    def __init__(self):

        self.largoChasis=250
        self.anchoChasis=120
        self.__ruedas=4         #Encapsulamiento (restringe cambios fuera de la clase)
        self.enmarcha=False

    # def arrancar(self):
    #     self.enmarcha=True

    def arrancar(self, arrancamos):

        self.enmarcha=arrancamos

        if(self.enmarcha):
            return "El coche esta en marcha."

        else:
            return "El coche esta parado."

    def estado(self):

        print("El coche tiene ", self.__ruedas, "ruedas, un ancho de ", self.anchoChasis, "y un largo de ",
        self.largoChasis)

toyota=Coche()

print(toyota.arrancar(True))

toyota.estado()

# AQUI EMPIEZA EL VIDEO 27

print("******** A continuacion creamos el segundo objeto ********")

nissan=Coche()

print(nissan.arrancar(False))

nissan.ruedas=2

nissan.estado()


