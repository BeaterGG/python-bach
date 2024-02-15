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

class perros(animal):
    def __init__(self,fuerza):
        super.__init__(fuerza)
        self.size=3
    def propiedades(self):
        print("Tamaño -->",self.size)
        return super().propiedades()



fuerza=int(input("Introduce el valor de 'fuerza' del objeto a crear: "))
perro1=perros(fuerza)

perro1.propiedades()