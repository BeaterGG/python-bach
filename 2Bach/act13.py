class Usuario():
    def __init__(self, name, password):
        """ método contructor con propiedades nombre y passord protegido"""
        
        self.name = name
        self.__password = password #la contraseña SI esta protegida

    def mostrarUsuario(self):
        """ solicita la contraseña actual y con el método protegido comprueba si son iguales, en ese caso muestra el nombre del usuario y la contraseña"""
        
        contra = input("Introduce el valor de la contraseña actual: ")
        if Usuario.modulcomprobarcontrasenya(self,contra)==True:
            print("\nLas propiedades del objeto",self.name,"son:\n====================================\nNombre de usuario:",self.name,"\nContraseña del usuario:", self.__password)

    def cambiarpassword(self):
        """ cambia la contraseña si el método protegido devuelve True """
        
        newpass=input("Introduce la nueva contraseña del objeto "+self.name+": ")
        contra = input("Introduce el valor de la contraseña actual: ")
        if Usuario.modulcomprobarcontrasenya(self,contra)==True:
            self.__password=newpass
            print("Contraseña cambiada a",self.__password)

    def cambiarnombre(self):
        """ pide la contraseña actual, comprueba que es la que tiene el usuario con el método protegido para permitir o no permitir el cambio de nombre de usuario"""
        
        newname=input("Introduce el nuevo nombre del objeto "+self.name+": ")
        contra = input("Introduce el valor de la contraseña actual: ")
        if Usuario.modulcomprobarcontrasenya(self,contra)==True:
            self.name=newname
            print("Nombre cambiado a",self.name)
        
    def __comprobarContrasenya(self,contra):
        """ método protegido, sólo se usa dentro del objeto devuelve True si contra es igual a self.__password """
        
        if self.__password==contra:
            return True
        else:
            return False
        
    def modulcomprobarcontrasenya(self,contra):
        """ si contra es igual self.__password mostrará contraseña válida en caso contrario mostrará contraseña incorrecta, Usa el método protegido"""
        
        if Usuario.__comprobarContrasenya(self,contra)==True:
            print("Contraseña válida. Acceso concedido")
            return True
        else:
            print("Contraseña Incorrecta")
            return False

nom = input("Nombre de usuario: ")
contrasenya = input("Contraseña: ")
usu1=Usuario(nom, contrasenya)

while True:
    print("""=================================\n- Menú de configuración de usuario:\n=================================\n\na. Mostrar el nombre del usuario. \nb. Mostrar el nombre y la contraseña del usuario. \nc. Cambiar el nombre del usuario. \nd. Cambiar la contraseña del usuario. \ne. Ejecutar el módulo de control de contraseña \nf. Salir del programa.\n\n        presione g para forzar el cambio de usuario a ¨Pedro¨ y de contraseña a ¨adios¨\n""")

    i = input("Selecciona opción: ")
    if i.lower() == "a":
        print("Nombre de  usuario: ",usu1.name)
    elif i.lower() == "b":
        usu1.mostrarUsuario()
    elif i.lower() == "c":
        usu1.cambiarnombre() 
    elif i.lower() == "d":
        usu1.cambiarpassword()
    elif i.lower() == "e":
        contra = input("Introduce el valor de la contraseña actual: ")
        usu1.modulcomprobarcontrasenya(contra)
    elif i.lower() == "f":
        print("Adios")
        break

    elif i.lower() == "g":
        usu1.__password="adios"
        usu1.name="Pedro"
        print("Se ha intentado forzar el cambio de usuario a ¨Pedro¨ y de contraseña a ¨adios¨\nCompruebe si se efectuaron los cambios")
        usu1.mostrarUsuario()


    else:
        print("Introduzca una opcion válida")