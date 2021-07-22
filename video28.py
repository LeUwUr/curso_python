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
            chequeo=self.chequeo_interno()

        if(self.enmarcha and chequeo):
            return "El coche esta en marcha."

        elif(self.enmarcha and chequeo==False):
            return"Algo ha salido mal. No se puede arrancar."

        else:
            return "El coche esta parado."

    def estado(self):

        print("El coche tiene ", self.__ruedas, "ruedas, un ancho de ", self.anchoChasis, "y un largo de ",
        self.largoChasis)

 #AQUI EMPIEZA VIDEO 28

    def chequeo_interno(self):
        print("Realizando chequeo interno...")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        
        else:
            return False

toyota=Coche()

print(toyota.arrancar(True))

toyota.estado()

# AQUI EMPIEZA EL VIDEO 27

print("******** A continuacion creamos el segundo objeto ********")

nissan=Coche()

print(nissan.arrancar(False))

nissan.estado()