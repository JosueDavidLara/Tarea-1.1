class Calculadora:
    def sumar(self, a: float, b: float):
        return a + b

    def restar(self, a: float, b: float):
        return a - b

    def multiplicar(self, a: float, b: float):
        return a * b

    def dividir(self, a: float, b: float):
        if b == 0:
            return "Error: No se puede dividir por cero"
        return a / b


calculadora = Calculadora()

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

print(f"Suma: {calculadora.sumar(a,b)}")
print(f"Resta: {calculadora.restar(a,b)}")
print(f"Multiplicación: {calculadora.multiplicar(a,b)}")
print(f"División: {calculadora.dividir(a,b)}")
