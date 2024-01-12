import random
n=random.randint(1,100)
x=6
while x!=0:
    r=int(input("Adivina un numero secreto entre 1 y 100 (tienes 6 intentos):"))
    if r==n:
        print("Correcto! El numero era",n)
        break
    elif r<n:
        print("El numero secreto es mayor que",r)
        print("Prueba otra vez")
    else:
        print("El numero secreto es menor que",r)
        print("Prueba otra vez")
    x=x-1
print("Te has quedado sin intentos, reinicia para volver a jugar con un numero nuevo")