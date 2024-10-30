
divisas = {
    'dolar':'$',
    'euro':'€', 
    'libra':'£'
}


divisa = input("Ingrese una divisa: euro, dolar, libra: ")

divisa = divisa.lower()

seleccion = divisas.get(divisa, "Divisa no encontrada")

print(seleccion)

