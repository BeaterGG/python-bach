def valida_opcion():
    while True:
        print("\n","============================","\n","GAMIFICACIÓN EN EL AULA".center(27),"\n","============================","\n","1 - Cargar datos del fichero","\n","2 - Imprimir datos","\n","3 - Jugar","\n","4 - Guardar datos","\n","5 - Cambiar contraseña","\n","0 - SALIR","\n","----------------------------","\n")
        opc=int(input("Elija una opción: "))
        if 0 <= opc <= 5:
            print("La opción seleccionada es",opc)
        else:
            print("Por favor, elija una opción válida")

valida_opcion()