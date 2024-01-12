import volumenes
import areas


print("Que quieres calcular")
print("1 - Area de un circulo dado su radio")
print("2 - Volumen de una esfera dado su radio")
print("3 - Volumen de un cubo dado su arista")
print("4 - Area de un triángulo dado su base y altura")
print("5 - Para salir")

x=0


while x!=5:
    try:
        x=int(input("Elige un numemero:"))
    except:
        print("Solo puedes introducir números!")
    if x==2:
        r=int(input("Dime el radio de la esfera:"))
        volumenes.vole(r)
    elif x==1:
        r=int(input("Dime el radio del circulo:"))
        areas.area_circulo(r)
    elif x==3:
        r=int(input("Dime la arista del cubo:"))
        volumenes.volc(r)
    elif x==4:
        r=int(input("Dime la base del triangulo:"))
        s=int(input("Dime su altura:"))
        areas.area_triangulo(r,s)
    elif x>5:
        print("Solo numeros entre el 1 y el 5!!")
    elif x==0:
        print("Solo numeros entre el 1 y el 5!!")
        
if x==5:
    print("Adios!")
    exit()

