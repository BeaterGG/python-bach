amigos=[]
amigos.append(input("Dime el nombre de uno de tus amigos (escribe fin para terminar): "))

while (amigos!="fin"):
    amigos.append(input("Dime el nombre de otro de tus amigos: "))
    if "fin" in amigos:
        amigos.remove("fin")
        print("El primer amigo en el que pensaste fue", amigos[0])
        print("El ultimo amigo en el que pensaste fue", amigos[-1])
        break