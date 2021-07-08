print("Programa de Becas 'EL BENITO'")

distancia_escuela=int(input("Introduce la distancia a la escuela en KM:"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos:"))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual familiar:"))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
    print("Tienes derecho a beca.")

else:
    print("No tienes derecho a beca, chale.")