import random
lista = []
a=0
while True:
    try:
        x = int(input("Dame una lista de números (introduce -1 para acabar): "))
        lista.insert(a,x)
        a+=1

        if x==-1:
            lista.remove(-1)
            print("\nLa lista original es: ",lista)

            print("\nOperemos con ella...")

            print("    -Tiene",len(lista),"números")

            listaordenada=sorted(lista)
            print("    -La lista ordenada es: ",listaordenada)

            print("    -El número aleatorio elegido es: ",random.choice(lista))
            print("\nHasta printo")
            break
    except:
        print("Eso no es un numero")

    