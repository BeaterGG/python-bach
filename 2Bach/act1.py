import math
usr=input("Introduzca su nombre de usuario: ")
print("Bienvenid@", usr, "dal programa de la unidad 1")
txt=input("Dame una cadena de texto y te digo cuantos caracteres tiene: ")
print("Esa cadena de texto tiene",len(txt),"caracteres")
rad=float(input("Dame el radio de un circulo y te dire su area: "))
area=rad**2*math.pi
areared=round(area, 4)
print("El area del circulo de radio", rad,"es:",areared)