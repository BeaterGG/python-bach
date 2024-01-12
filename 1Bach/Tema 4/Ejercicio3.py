n1=int(input("Dime un numero y te digo sus divisores:"))

for d in range(1,n1+1):
    if (n1 % d) == 0:
        print(d,"es divisor de",n1)