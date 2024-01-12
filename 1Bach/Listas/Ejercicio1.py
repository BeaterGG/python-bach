amigos=[]
amigos.append(input("Dime el nombre de uno de tus amigos (escribe fin para terminar): "))

while (amigos!="fin"):
    amigos.append(input("Dime el nombre de otro de tus amigos: "))
    if "fin" in amigos:
        amigos.remove("fin")
        print("Tienes",len(amigos),"amigos y son:", amigos)
        break