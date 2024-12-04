import hashlib

# Contraseña original que deseas hashear
password = "mipassword"

# Crear un objeto de hash SHA-256 y obtener el hash de la contraseña original
hash_obj = hashlib.sha256(password.encode('utf-8'))
password_hash = hash_obj.hexdigest()

print("Hash SHA-256:", password_hash)

# Simulación de ingreso de contraseña
in_password = input("Ingrese su contraseña: ")

# Crear un nuevo objeto de hash SHA-256 para el input y calcular su hash
in_hash_obj = hashlib.sha256(in_password.encode('utf-8'))
in_password_hash = in_hash_obj.hexdigest()

print("Hash ingresado:", in_password_hash)

# Comparar los hashes
if in_password_hash == password_hash:
    print("Las claves coinciden")
else:
    print("Las claves no coinciden")
