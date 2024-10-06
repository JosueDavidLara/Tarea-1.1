def generar_tabla(numero):
    for _ in range(10):
        print(f"{numero}x{_+1}={numero*(_+1)}")


n = int(input("Ingrese el número de términos: "))
generar_tabla(n)
