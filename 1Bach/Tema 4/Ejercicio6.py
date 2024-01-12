palabra = []
palabra.append(input("Escribre una palabra para añadirla a tu lista: "))
print("")
print("Tu lista de palabras por el momento se ve asi:", palabra[0])
n = len(palabra)-1
while palabra[n] != (""):
    print("")
    palabra.append(input("Escribe otra palabra para añadirla a tu lista: "))
    if palabra[n] != (""):
        print("")
        print("Tu lista de palabras ahora tiene",len(palabra), "palabras",)
        print("")
        print("Tu lista de palabras ahora es:")
        for x in palabra:
            print("-",x)
        n = n+1