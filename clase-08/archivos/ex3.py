archivo = open("texto_escritura.txt", "a")


archivo.write("Informacion al archivo\n")

archivo.close()

# Da error porque el archivo ya esta cerrado
# archivo.write("Informacion al archivo\n")