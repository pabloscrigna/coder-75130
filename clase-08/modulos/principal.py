

# forma 1

""""
import funciones_matematicas
"""


# forma 2

""""
from funciones_matematicas import *
"""

# forma 3

from funciones_matematicas import suma, resta, OP
from func_matematicas import suma as suma_tres

num1 = 5
num2 = 9

# forma 1
# resultado = funciones_matematicas.suma(num1, num2)

resultado = suma(num1, num2)

print(f"el resutado de la suma es {resultado}")

resultado = resta(num1, num2)

print(f"el resutado de la resta es {resultado}")

print(OP)

print(suma_tres(5,7,8))