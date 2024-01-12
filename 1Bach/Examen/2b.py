print("-------------------------------------")
print("Calculador de volumen de esferas (2b)")
x=1
s="s"
vv=[]
rr=[]
import time , sys
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
                vv2 = [x for x in vv if x < 32]
                print("-------------------------------------")
                print("Voy a eliminar las esferas con poco volumen:", vv2)
                total = 1007
                bar_length = 30
                for i in range(total+1):
                    percent = 100.0*i/total
                    sys.stdout.write('\r')
                    sys.stdout.write("Eliminando: [{:{}}] {:>3}%"
                     .format('='*int(percent/(100.0/bar_length)),
                             bar_length, int(percent)))
                    sys.stdout.flush()
                    time.sleep(0.002)
                vv3 = [x for x in vv if x > 32]
                print("")
                print("-------------------------------------")
                print("Volúmenes de esferas grandes:",vv3)
                print("------------------Adiós!!-------------------")
                break