numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese un numero: "))
  
operacion = "+"
    
if operacion == "+":
    resultado = numero1 + numero2
else:
    resultado =  numero1 - numero2
  
print(f"El resultado de {numero1} {operacion} {numero2} es {resultado}")

