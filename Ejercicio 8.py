def contar_vocales(frase):
    vocales = "aeiouAEIOU"
    contador = 0

    for letra in frase:
        if letra in vocales:
            contador += 1
    return contador


frase_usuario = input("Ingrese una frase: ")
frase_prueba = "Y si me retiro de la Universidad, pero me doy de baja para luego no poder volver?"  # 29
print(f"El número total de vocales en la frase es: {contar_vocales(frase_usuario)}")
