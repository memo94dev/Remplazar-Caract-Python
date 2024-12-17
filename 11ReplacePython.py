'''
Modificar el programa para resolver el ejercicio, no modificar la impresión
'''
# Solicitar al usuario ingresar una cadena de texto
cadena = input("Ingresar una cadena de texto: ")


# Codificar la cadena original

cadena_codificada = cadena.replace("a","1").replace("e","2").replace("i","3").replace("o","4").replace("u","5")


# Imprimir la cadena codificada, no modifique el formato de impresión, requerido para la calificación
print(f"La cadena codificada es: {cadena_codificada}")
