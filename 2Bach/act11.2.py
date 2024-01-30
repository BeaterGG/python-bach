class triangulo:
    def __init__(self,base,altura) -> None:
        tipo="Triángulo"
        lados=3
        self.tipo = tipo
        self.lados = lados
        self.base = base
        self.altura = altura
        self.area=self.altura*self.base/2
    def props(self):
        print("Numero de lados:", self.lados)
        print("Tipo de polígono:", self.tipo)
        print("Base:", self.base)
        print("Altura:", self.altura)
    def propsarea(self):
        print("Base:", self.base)
        print("Altura:", self.altura)
        print("El area es:", round(self.area,2))
         
t1 = triangulo(5,4)

print("\n---- Datos del segundo triángulo ---")
base=float(input("Introduce la longitud de la base: "))
altura=float(input("Introduce la longitud de la altura: "))
t2= triangulo(base,altura)

print("\n-------- Propiedades del primer triángulo--------")
t1.propsarea()
print("\n-------- Propiedades del segundo triángulo--------")
t2.propsarea()