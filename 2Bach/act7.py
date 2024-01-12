def saludo():
    ln=input("¿Quieres el saludo en castellano o valenciano (cs/va)?: ")
    if ln.lower()=="cs":
        print("Buenos días")
    else:
        print("Bon día")

def estrellas():
    try:
        s=int(input("Dime el numero de estrellas que quieres: "))
        print(("*")*s)
    except:
         print("ERROR. Se esperaba un número.")

def escalera():
    try:
        n=int(input("Dame un numero para hacer una escalera de estrellas: "))
        a=1
        if a<=n:
            print(("*")*a)
            a+=1
        else:
             print("ERROR. Se esperaba un número mayor que 0.")
    except:
         print("ERROR. Se esperaba un número entero.")

def dibuja_escalera_personalizada(a,n,t):
    while a<=n:
        print(t*a)
        a+=1

def escalera_personalizada():
    n=int(input("Dame un numero para hacer una escalera: "))
    t=input("Dame el texto que quieras utilizar: ")
    a=1
    dibuja_escalera_personalizada(a,n,t)

while True:
    print("\n","============================","\n","MISCELÁNEA".center(27),"\n","============================","\n","1 - Saludo castellano/valenciano","\n","2 - Estrellas","\n","3 - Escalera de estrellas","\n","4 - Escalera personalizada","\n","0 - SALIR","\n","----------------------------","\n")
    opc=(int(input("Dame la opción:")))
    if 0 <= opc <= 4:
            if opc==1:
                 saludo()
            elif opc==2:
                 estrellas()
            elif opc==3:
                 escalera()
            elif opc==4:
                 escalera_personalizada()
            elif opc==0:
                 print("Hasta luego")
                 break
                 
    else:
        print("Por favor, elija una opción válida")