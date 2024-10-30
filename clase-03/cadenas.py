"""
Transforma el texto en:

Gordon lanzó su curva...

Strawberry ha fallado por un pie! -gritó Joe Castiglione.

Dos pies le corrigió Troop.

Strawberry menea la cabeza como disgustado… -agrega el comentarista.

"""

frase = "gordon lanzó su curva&strawberry ha fallado por un pie!" 
frase = f"{frase} -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry" 
frase = f"{frase} menea la cabeza como disgustado… -agrega el comentarista"

# print(frase)

lista_frase1 = frase.split("&")

print(f"{lista_frase1[0].capitalize()}...")

# frase1 = frase1.capitalize()
# print(frase1)

# print(lista_frase1[1])

print(f"{lista_frase1[1][0].upper()}{lista_frase1[1][1:]}")


print(lista_frase1)