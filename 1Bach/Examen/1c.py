print("-------------------------------------")
print("Calculador de volumen de esferas (1c)")
x=1
s="s"
vv=[]
rr=[]
while s=="s" or s=="S":
    while x!=0:
        try:
            print("-------------------------------------")
            r=int(input("Dime el radio de la esfera: "))
            rr.append(r)
        except:
            print("El radio debe ser un numero")
        else:
            x=x-1
            v=4/3*3.14*r**3
            vv.append(v)
            print("Para un radio de",r,"el volumen de la esfera será",v)
            s=input("Desea continuar (sS): ")
            if s=="s" or s=="S":
                x=x-1
            else:
                print("-------------------------------------")
                print("Radios:",rr)
                print("Volúmenes:",vv)
                print("------------------Adiós!!-------------------")
                break