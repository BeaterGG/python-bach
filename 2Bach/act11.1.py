class triangulo:
    def __init__(self,base,altura) -> None:
        tipo="Triángulo"
        lados=3
        self.tipo = tipo
        self.lados = lados
        self.base = base
        self.altura = altura
    def props(self):
        print("Numero de lados:", self.lados)
        print("Tipo de polígono:", self.tipo)
        print("Base:", self.base)
        print("Altura:", self.altura)

t1 = triangulo(5,4)

print("\n---- Datos del segundo triángulo ---")
base=input("Introduce la longitud de la base: ")
altura=input("Introduce la longitud de la altura: ")
t2= triangulo(base,altura)

print("\n-------- Propiedades del primer triángulo--------")
t1.props()
print("\n-------- Propiedades del segundo triángulo--------")
t2.props()