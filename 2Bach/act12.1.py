class Triangulo:
    def __init__(self,lado1,lado2,lado3) -> None:
        lados=3
        self.lados = lados
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    def props(self):
        print("Número de lados:",self.lados)
        print("Lado 1:",self.lado1)
        print("Lado 2:",self.lado2)
        print("Lado 3:",self.lado3)
    def longer(self):
        print("El lado mas largo mide:",max(self.lado1,self.lado2,self.lado3))
    def tipo(self):
        if self.lado1==self.lado2==self.lado3:
            print("Triángulo Equilatero")
        elif self.lado1==self.lado2 or self.lado2==self.lado3 or self.lado1==self.lado3:
            print("Triángulo Isosceles")
        else:
            print("Triángulo Escaleno")

while True: 
    try:
        lado1=float(input("Longitud del primer lado: "))
        lado2=float(input("Longitud del segundo lado: "))
        lado3=float(input("Longitud del tercer lado: "))
        break
    except:
        print("Eso no es un dato valido (número). Comienza de nuevo")
t1=Triangulo(lado1,lado2,lado3)

t1.props()
t1.longer()
t1.tipo()