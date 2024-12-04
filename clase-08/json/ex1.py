import json

# objeto python
datos_persona = {

    "nombre": "Juan",
    "edad": 45,
    "peso": 60.7,
    "activo": True,
    "curso": None,
    "notas": (5, 8),
    "cursos": ["A", "B"]

}

print(f"datos dict python: {datos_persona}")
print(f"tipo de dato: {type(datos_persona)}")

# pasamos el objeto python a un string json (serializar)
datos_persona_json = json.dumps(datos_persona)

print(f"datos persona en json: {datos_persona_json}")
print(f"tipo de dato: {type(datos_persona_json)}")

# pasar el string json a un objeto python

datos_persona_obj = json.loads(datos_persona_json)

print(f"datos persona en objecto python: {datos_persona_obj}")
print(f"tipo de dato: {type(datos_persona_obj)}")
