import random

def lee_lista():
    """crea una lista y va introduciendo los numeros dados por el usuario en ella"""
    lista = []
    a=0
    while True:
        try:
            x = int(input("Dame una lista de números (introduce -1 para acabar): "))
            lista.insert(a,x)
            a+=1
            if x==-1:
                lista.remove(-1)
                return lista
        except:
            print("Eso no es un numero")

def operando(lista):
    """interpreta la lista y devuelve una tupla con la longitud de la lista original, una nueva lista con los valores ordenados de menor a mayor y un valor seleccionado al azar de la lista original"""
    a=len(lista)

    listaordenada=sorted(lista)
    b=listaordenada

    c=random.choice(lista)
    return (a,b,c)
lista=lee_lista()
print(lista)

a,b,c, = operando(lista)

print("    -Tiene",a,"números")
print("    -La lista ordenada es: ",b)
print("    -El número aleatorio elegido es: ",c)
