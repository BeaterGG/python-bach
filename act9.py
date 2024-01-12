def imprimir(jugadora):
    print("\n","--- IMPRIMIR DATOS JUGADORA ---")
    print()
    if len(jugadora)==0:
            print("No hay ningún dato")
    else:
        for key in jugadora.keys():
            print(key,"-->",jugadora.get(key))
        
def imprimir_claves(jugadora):
    print("\n","--- IMPRIMIR CLAVES ---")
    print("CLAVES:",", ".join(jugadora.keys()))

def consultar_valor(jugadora):
    print("\n","--- CONSULTAR UN VALOR ---")
    val=input("¿Qué clave quieres consultar? ")
    try:
        print(val,"--->",jugadora[val])
    except:
        print("Lo siento pero esa clave no existe")
        
def anyadir_edad(jugadora):
    print("\n","--- AÑADIR EDAD ---")
    try:
        ed=int(input("Dame la edad: "))
        jugadora.update({"edad":ed})
        print("Edad de la jugadora actualizada")
    except:
        print("Eso no es un número")
        print("No se ha actualizado la edad")
    return jugadora

def borrar_clave(jugadora):
    print("\n","--- BORRAR CLAVE ---")
    c=input("¿Qué clave quieres borrar? ([INTRO] para regresar al menu) ")
    if c in jugadora.keys():
        print("BORRADO",c,"-->",jugadora.get(c))
        jugadora.pop(c)
    elif c=="":
        print("No se ha eliminado ninguna clave")
    else:
        print("Lo siento pero esa clave no existe")
    return jugadora    

jugadora = {'nombre':'Mafalda','personaje':'sabia','herramientas':['varita','conjuro','sombrero','buho'],'vida':100}
menu = """
        1 - Imprimir datos de jugadora
        2 - Imprimir claves
        3 - Consultar valor
        4 - Añadir <edad>
        5 - Borrar clave
        0 - Salir jeje"""
while True:
    print("\n","--- MAIN MENU ---")
    print(menu,"\n")
    o = input("Selecciona opción: ")
    if o == '0':
        break
    elif o == '1':
        imprimir(jugadora)
    elif o == '2':
        imprimir_claves(jugadora)
    elif o == '3':
        consultar_valor(jugadora)
    elif o == '4':
        jugadora = anyadir_edad(jugadora)
    elif o == '5':
        jugadora = borrar_clave(jugadora)
        
        