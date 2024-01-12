n=int(input("Dame un numero entero del 1  al 10: "))
a=1
if n>=1 and n<=10:
    print("LA TABLA DE MULTIPLICAR DEL Nº",n)
    while a<11:
        print(a,"x",n,"=",a*n)
        a+=1
else:
    print("Eso no es un numero del 1 al 10")