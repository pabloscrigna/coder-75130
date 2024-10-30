"""
A partir de una lista realizar las siguientes tareas sin modificar la lista original:

1. Borrar los elementos duplicados

2. Ordenar la lista de mayor a menor

Eliminar todos los números impares ( for num in lista if (num%2==1) ---- pop, remove )

Realizar una suma de todos los números que quedan (sum(lista))

Añadir como primer elemento de la lista la suma realizada insert(0, suma)

Devolver la lista modificada

Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

"""

lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

lista_1 = list(set(lista))

print(f"lista original : {lista}")

print(f"sin repetidos: {lista_1}")

lista_1.sort()
print(f"lista sin repetidos ordenada de menor a mayor {lista_1}")


print(f"lista_1 : {lista_1}")
suma = sum(lista_1)
print(f"suma de todos los elementos de lista: {suma}")

lista_1.insert(0, suma)

print(f"lista_1 con la suma: {lista_1}")
