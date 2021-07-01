midiccionario={"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","Mexico":"Ciudad de Mexico"} #"palabra":"significado"

midiccionario["Italia"]="Lisboa"  #aniade un nuevo elemento al diccionario

print(midiccionario)  #imprime todo el diccionario
print(midiccionario["Francia"]) #la funcion imprime lo que se busca

midiccionario["Italia"]="Roma" #corrige el valor de una palabra y se imprime el nuevo
print(midiccionario)

del midiccionario["Reino Unido"] #elimina un elemento indicado
print(midiccionario)

diccionario1={23:"Jordan","mosqueteros":3}
print(diccionario1)

mitupla=["Espania","Francia","Reino Unido","Alemania"]
diccionario2={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}

print(diccionario2)
print(diccionario2["Francia"])

dicc={23:"Eva","Nombre":"Michael","Equipo":"Chicago","Anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}

print(dicc.keys()) #imprime claves
print(dicc.values())  #imprime valores
print(len(dicc))

print(dicc)
print(dicc["Equipo"])
print(dicc["Anillos"])
