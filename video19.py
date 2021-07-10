def generador(limite):
    num=1
    
    while num<limite:

        yield num*2

        num=num+1

devuelvePar=generador(10)

print(next(devuelvePar))

print("Aqui podria ir mas codigo.")
print(next(devuelvePar))

print("Aqui podria ir mas codigo..")
print(next(devuelvePar))