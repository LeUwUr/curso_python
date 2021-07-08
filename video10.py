print("Programa de EVAluacion de notas de alumnos")

nota_alumno=input("Introduce nota del alumno:")

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:  # >Mayor que / <Menor que / == Igual que / >=/ <= / != Diferente que
        valoracion="reprobado"
    return valoracion

#print(evaluacion(4)) #debe devolver reprobado /aqui hay un valor definido

print(evaluacion(int(nota_alumno)))