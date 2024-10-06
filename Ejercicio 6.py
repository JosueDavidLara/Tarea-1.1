def fibonacci(n):
    a = 0
    b = 1
    secuencia = []

    for _ in range(n):
        secuencia.append(str(a))
        temp = a
        a = b
        b = temp + b

    print(", ".join(secuencia))


n = int(input("Ingrese el número de términos: "))
fibonacci(n)
