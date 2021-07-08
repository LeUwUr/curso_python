print("Asignaturas optativas UWU")

print("Asignaturas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida:")

asignatura=opcion.lower() #condiciona a hacer minusculas sin necesidad de escribirlo correctamente

if asignatura in ("informatica grafica","pruebas de software","usabilidad y accesibilidad"):
    print("Asignatura elegida:" + asignatura)

else:
    print("La asignatura escogida no esta contemplada.")