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
    def __init__(self,fuerza,size):
        super().__init__(fuerza)
        self.size=size
    def propiedades(self):
        print("\nPropiedades del perro:")
        super().propiedades()
        print("Tamaño -->",self.size)
        
    def __str__(self):
        return(f"Este perro tiene {self.fuerza} puntos de fuerza, {self.vida} puntos de vida y un tamaño de {self.size}")

fp=int(input("\nIntroduce el valor de 'fuerza' del primer objeto a crear: "))
size=int(input("Introduce el valor de 'tamaño' del primer objeto a crear: "))
perro1=Perros(fp,size)

perro1.propiedades()
print(perro1)
