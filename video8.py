mitupla=("eva", 29, 3, 2001, 13) #a las tuplas no se les puede aniadir elementos exteriores
milista=list(mitupla)

lista=["mariana", 8, 6, 2021, 6]
mitupla=tuple(lista)

print(mitupla[2]) # imprime la posiscion de un elemento indicado
print(milista) #imprime los elementos dentro de cotchetes
print(mitupla) #imprime los elementos dentro de parentesis

print("eva" in milista) #True/False de un elemento dentro de una lista

print(mitupla.count(6)) #cuenta las veces que esta el elemento indicado dentro de la tupla

print(len(mitupla)) #te da cuantos elementos hay

tupla=("jordan",) #coma para tupla unitaria
print(len(tupla))

tupla2="frijol", 2, 4, 2006 #otro tipo de tupla sin corchetes o parentesis / empaquetado de tupla
print(tupla2)

nombre, dia, mes, anio= tupla2 #desempaquetado de tuplas
print(nombre)
print(mes)
print(anio)
print(dia)