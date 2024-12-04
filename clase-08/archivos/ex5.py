# Context manager


# readline
with open("texto.txt", "r") as archivo:
    linea = archivo.readline()
    print(f"la primera linea es: {linea}")
    linea = archivo.readline()
    print(f"la segunda linea es: {linea}")


# el archivo ya esta cerrado
print("continua el programa")    


# readlines
with open("texto.txt", "r") as archivo:
    lineas = archivo.readlines()


print(lineas)

for linea in lineas:
    print(linea)


with open("texto.txt", "r") as archivo:
    for linea in archivo.readlines():
        print(linea)