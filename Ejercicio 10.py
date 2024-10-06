import random
import string


def generar_contrasena(longitud):
    if longitud < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
    else:
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = "".join(random.choice(caracteres) for _ in range(longitud))
        print(f"Contraseña generada: {contrasena}")


longitud_usuario = int(
    input("Ingrese la longitud de la contraseña (mínimo 8 caracteres): ")
)

generar_contrasena(longitud_usuario)
