print("Este programa muestra la suma y la media de los numeros que introduzcas")

num = []
num.append((input("Escribe un número para añadirlo a la lista: ")))

n = len(num)-1

try:
 while num[n] != (""):
    num.append((input("Escribe otro numero para añadirlo a la lista: ")))
    if num[n] != (""):
        num1 = list(map(int, num))
        print("Hasta el momento has introducido",len(num),"numeros")
        print(num1)
        print("La suma total es:",sum(num1))
        print("Y la media es:", sum(num1)/len(num1))
        n = n+1
except:
   print("Debes introducir numeros")
   while n:
      break