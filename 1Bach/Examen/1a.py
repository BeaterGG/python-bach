print("-------------------------------------")
print("Calculador de volumen de esferas (1a)")
x=1
while x!=0:
    try:
        print("-------------------------------------")
        r=int(input("Dime el radio de la esfera: "))
    except:
        print("El radio debe ser un numero")
    else:
        v=4/3*3.14*r**3
        print("Para un radio de",r,"el volumen de la esfera será",v)
        x=x-1