import random

numero_aleatorio = random.randint(1, 100)
intentos = 0

print("Adivina el número entre 1 y 100!")

while True:
    numero_usuario = int(input("Ingresa tu intento: "))
    intentos += 1
    if numero_usuario < numero_aleatorio:
        print("El número es mayor.")
    elif numero_usuario > numero_aleatorio:
        print("El número es menor.")
    else:
        print(f"¡Felicitaciones! Has adivinado el número en {intentos} intentos.")
        break
