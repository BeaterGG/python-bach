print("Analizador de palabras 2.0")
palabra=input("Escribe una palabra:")
print("La palabra",palabra,"tiene",len(palabra),"caracteres")
if len(palabra)<=5:
    print("La primera letra es:",(palabra[:1]))
    print("La ultima letra es:",(palabra[-1:]))
else:
    print("Las cuatro primeras letras son:",(palabra[:4]))
    print("Las cuatro ultimas letras son:",(palabra[-4:]))