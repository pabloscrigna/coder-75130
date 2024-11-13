# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

# sumar todos los valor y dividirlos por la cantida de elementos

lista_demo = [6,7,8]


def media(lista):

    cantidad = len(lista)

    acumulador = 0
    for valor in lista:
        acumulador += valor

    valor_medio = acumulador / cantidad

    return valor_medio 


print(media(lista_demo))
print(media([3,3,3]))

print(media((5,6,4)))