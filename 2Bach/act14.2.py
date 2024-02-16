class Animal():
    def __init__(self,fuerza):
        self.vida=10
        if fuerza<=5:
            self.fuerza=fuerza
        else:
            pass
    def propiedades (self):
        
        print("Vida -->",self.vida)
        print("Fuerza -->",self.fuerza)

class Perros(Animal):
    def __init__(self,fuerza):
        super().__init__(fuerza)
        self.size=3
    def propiedades(self):
        print("\nPropiedades del perro:")
        super().propiedades()
        print("Tamaño -->",self.size)

class Gatos(Animal):
    def __init__(self,fuerza):
        super().__init__(fuerza)
        self.hambre=2
    def propiedades(self):
        print("\nPropiedades del gato:")
        super().propiedades()
        print("Hambre -->",self.hambre)

class Ratones(Animal):
    def __init__(self,fuerza):
        super().__init__(fuerza)
        self.color="blanco"
    def propiedades(self):
        print("\nPropiedades del ratón:")
        super().propiedades()
        print("Color -->",self.color)

fp=int(input("\nIntroduce el valor de 'fuerza' del primer objeto a crear: "))
perro1=Perros(fp)

perro1.propiedades()

fg=int(input("\nIntroduce el valor de 'fuerza' del segundo objeto a crear: "))
gato1=Gatos(fg)

gato1.propiedades()

fr=int(input("\nIntroduce el valor de 'fuerza' del tercer objeto a crear: "))
raton1=Ratones(fr)

raton1.propiedades()