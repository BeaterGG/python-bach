print()

err = 0

try:
 n = int(input("Calculadora de divisores: "))
except:
    print("No detecto ese numero")
    while err:
       break

print()

cont = 0

try:
 while n:
    for x in range(1,n+1):
        if (n % x) == 0:
            print(x,"es divisor de",n)
            cont = cont + 1
    print(n,"tiene",cont, "divisores")
    print()
    cont = 0
    n = int(input("Escribe otro numero: "))
    print("")
except:
   while err:
      break