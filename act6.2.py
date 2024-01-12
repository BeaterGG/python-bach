def lee_nombre(): 
    """recibe el nombre de usuario y lo devuelve"""
    print("DIME QUIÉN ERES")
    name=input("Escribe tu nombre: ")
    return name

def sel_idioma():
    """permite al usuario seleccionar el idioma (castellano, valenciano o ingles)"""
    print("SELECCIONA EL IDIOMA")
    while True:
        print("Idiomas disponibles: cs, va, en")
        lan=input("Idioma elegido: ")
        if lan.lower()=="cs" or lan.lower()=="va" or lan.lower()=="en":
            break
        else:
            print("ERROR. Idioma no disponible. Vuelve a intentarlo")
    return lan

def bienvenida(lan,name):
    """le da la bienvenida al usuario con la informacion dada por lee_nombre y sel_idioma"""
    print("BIENVENIDO")
    if lan.lower()=="cs":
        print("Bienvenido a mi programa,", name)
    elif lan.lower()=="va":
        print("Benvingut,",name)
    elif lan.lower()=="en":
        print("Welcome to the jungle,",name)

while True:
    print("\n","============================","\n","BIENVENIDA INTERNACIONAL".center(27),"\n","============================","\n","1 - Dime quién eres","\n","2 - Selecciona el idioma","\n","3 - Bienvenid@","\n","0 - SALIR","\n","----------------------------","\n")
    opc=int(input("Elija una opción: "))
    if 0 <= opc <= 3:
        if opc==1:
            name=lee_nombre()
        elif opc==2:
            lan=sel_idioma()
        elif opc==3:
            try:
                bienvenida(lan,name)
            except:
                print("Por favor ingresa un nombre y selecciona un idioma")
        elif opc==0:
            print("ADIÓS")
            break
    else:
        print("Por favor, elija una opción válida")