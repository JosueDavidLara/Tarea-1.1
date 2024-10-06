class Rectangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)


Rectangulo = Rectangulo(base=5, altura=3)
print(f"Area: {Rectangulo.area()} \nPerimetro: {Rectangulo.perimetro()}")
