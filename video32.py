class coche():

    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas.")

class moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas.")

class camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas.")

#miVehiculo=moto()
#miVehiculo.desplazamiento()

#miVehiculo2=coche()
#miVehiculo2.desplazamiento()

#miVehiculo3=camion()
#miVehiculo3.desplazamiento()

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=moto()
desplazamientoVehiculo(miVehiculo)
