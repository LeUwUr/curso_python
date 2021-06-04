milista = ["Maria", "Pepe", "Marta","Antonio"]

milista.append("Sandra") #agrega un elemento al final de la lista
milista.insert(2,"EVA") #incluye en una posicion indicada el elemento en la lista
milista.extend(["Karlo", "Carlos", "Mariana", "Lola", "Cesar"]) #agrega una nueva lista a la lista principal
milista.remove("Lola") #elimina el elemento especifico de una lista
milista.pop() #elimina ultimo elemento de la lista



print(milista[:])

milista2 = ["Frijol", "Jairo"]

milista3 = milista + milista2

print(milista3)

print(milista[2]) #variable para acceder a una posicion especifica de una lista

print(milista[-3]) #cuenta regresiva de una lista

print(milista[0:3]) #accede a los primeros elementos de la lista

print(milista.index("Antonio")) #indica la posicion del elemento

print("Pepe" in milista) # true/false si se encuentra el elemento en la lista

milista4 = ["Bañate"] *3 #repite los elementos de una lista

print(milista4[:])