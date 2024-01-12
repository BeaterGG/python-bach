amigos=[]
amigos.append(input("Dime el nombre de uno de tus amigos (escribe fin para terminar): "))

while (amigos!="fin"):
    amigos.append(input("Dime el nombre de otro de tus amigos: "))
    if "fin" in amigos:
        amigos.remove("fin")
        amigos.pop(0)
        print("La lista de simplemente amigos es", amigos)
        break