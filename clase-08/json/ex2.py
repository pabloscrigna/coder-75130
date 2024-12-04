import json


# vamos a leer el archivo y pasarlo a objeto python

with open("datos_json", "r") as archivo:
    alumnos_obj = json.load(archivo)


print(f"objeto python: {alumnos_obj}")


for alumno in alumnos_obj:
    alumno["tipo"] = "P"

print(alumnos_obj)

with open("datos_json", "w") as archivo:
    json.dump(alumnos_obj,archivo, indent=4)