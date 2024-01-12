while True:
    print("\n","============================","\n","MISCELANEA".center(25),"\n","============================","\n","1 - Saludo castellano/valenciano","\n","2 - Estrellas","\n","3 - Escalera de estrellas","\n","0 - SALIR","\n","----------------------------","\n")
    opc=(input("Dame la opción:"))
    if opc=="1":
        ln=input("¿Quieres el saludo en castellano o valenciano (cs/va)?: ")
        if ln.lower()=="cs":
            print("Buenos días")
        else:
            print("Bon día")
    elif opc=="2":
        s=int(input("Dime el numero de estrellas: "))
        print(("*")*s)
    elif opc=="3":
        n=int(input("Dame un numero: "))
        a=1
        while a<=n:
            print(("*")*a)
            a+=1
    elif opc=="0":
        print("Adiós!")
        break
    else:
        print(opc,"no es una opcion válida")