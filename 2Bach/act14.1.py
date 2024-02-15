class animal():
    def __init__(self,fuerza):
        self.vida=10
        if fuerza<=5:
            self.fuerza=fuerza
        else:
            pass
    def propiedades (self):
        print("Propiedades del animal:")
        print("Vida -->",self.vida)
        print("Fuerza -->",self.fuerza)


fuerza=int(input("Introduce el valor de 'fuerza' del objeto a crear: "))
a1=animal(fuerza)

a1.propiedades()