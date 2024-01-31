class triangulo:
    def __init__(self,base,altura) -> None:
        tipo="Triángulo"
        lados=3
        self.tipo = tipo #el dato de "lados" NO esta protegido
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

while True:
    try:
        base=float(input("Introduce la longitud de la base: "))
        altura=float(input("Introduce la longitud de la altura: "))
        break
    except:
        print("Eso no es un dato valido (número)")
t2= triangulo(base,altura)

print("\n-------- Propiedades del primer triángulo--------")
t1.props()
print("\n-------- Propiedades del segundo triángulo--------")
t2.props()