email=False

contador=0
mi_email=input("Introduce tu direccion de email:")

for i in mi_email:

    if(i=="@" or i =="."): # == compara
     contador=contador+1
    # email=True  # = asigna

if contador==2:
    print("Email es correcto.")

else:
    print("El email no es correcto.")
