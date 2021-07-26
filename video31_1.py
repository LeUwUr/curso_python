class persona():
    
    def __init__(self, nombre, edad, residencia):

        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia

    def descripcion(self):

        print("NOMBRE: ", self.nombre, "EDAD: ", self.edad, "RESIDENCIA: ", self.residencia)
        
class empleado(persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario=salario
        self.antiguedad=antiguedad

    def descripcion(self):
        super().descripcion()

        print("SALARIO: ", self.salario, "ANTIGUEDAD: ", self.antiguedad)

Manuel=empleado("1800", "3 anios", "Manuel", 55, "Mexico")

Manuel.descripcion()

print(isinstance(Manuel, empleado))