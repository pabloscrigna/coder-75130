# Dado un texto = "Hola mundo feliz contento
# y dado un diccionario con puntos asociados a cada palabra 
# calcular el promedio del texto
# si la palabra no esta su valor vale cero


texto = "hola mundo feliz contento"

diccionario = {
    "hola" : 5,
    "feliz": 10,
    "malo": 0,
    "enojado": -1,
    "contento" : 10
}


# promedio = (5 + 0 + 10 + 10) / 4


palabras = texto.split()

print(palabras)

acumulador = 0

for palabra in palabras:
    print(palabra)
    # if palabra in diccionario:
    #    print(f"la palabra {palabra} esta en el diccionario")
    #    acumulador += diccionario[palabra]   # diccionario.get(palabra)

    acumulador += diccionario.get(palabra, 0)


print(f"la suma de todas las palabras es: {acumulador}")

cantidad_palabras = len(palabras) 
print(f"la cantidad de palabras es {cantidad_palabras}")

promedio = acumulador / cantidad_palabras

print(f"el promedio del texto es {promedio}")


