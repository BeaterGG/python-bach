print("DIVIDAMOS NÚMEROS ENTEROS!")
while True:
    try:
        n1=int(input("DIVIDENDO: "))
        break
    except:
        print("ERROR: Se esperaba un número entero")
while True:
    try:
        n2=int(input("DIVISOR: "))
        print(n1,"/",n2,"=",n1//n2)
        break
    except ValueError:
        print("ERROR: Se esperaba un número entero")
    except ZeroDivisionError:
            print("ERROR: Se esperaba un número distinto de cero")