players = ["mario","mafalda","luigi","esther","Heidi"]
while True:
    try:
        print("\n","============================","\n","JUGADORES ON-LINE".center(27),"\n","============================","\n","1 - Llega un jugador nuevo","\n","2 - Se va un jugador","\n","3 - FIN","\n","----------------------------","\n")
        opc=int(input("Elija una opción: "))
        if opc == 1:
                newp=input("¿Quién eres? ")
                players.append(newp)
                print("LISTA ACTUAL DE JUGADORES: "," - ".join(players))
                
        elif opc == 2:
                print("Se va el jugador", players[0])
                players.pop(0)
                print("LISTA ACTUAL DE JUGADORES: "," - ".join(players))
        elif opc == 3:
                print("LISTA ACTUAL DE JUGADORES: "," - ".join(players))
                print("Hasta pronto")
                break
        else:
            print("Por favor, elija una opción válida")
    except:
        print("Por favor, elija una opción válida")