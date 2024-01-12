print("-------------------------------------")
print("Calculador de volumen de esferas (1b)")
x=1
s="s"
while s=="s" or s=="S":
    while x!=0:
        try:
            print("-------------------------------------")
            r=int(input("Dime el radio de la esfera: "))
        except:
            print("El radio debe ser un numero")
        else:
            x=x-1
            v=4/3*3.14*r**3
            print("Para un radio de",r,"el volumen de la esfera será",v)
            s=input("Desea continuar (sS): ")
            if s=="s" or s=="S":
                x=x-1
            else:
                print("------------------Adiós!!-------------------")
                break