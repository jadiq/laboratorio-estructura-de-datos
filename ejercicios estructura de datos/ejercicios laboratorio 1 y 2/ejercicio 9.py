## ejercicio 9 ###
#Cuenta el número de vocales en una cadena de texto.
def contar_vocales(cadena):
    """
    Función que cuenta el número de vocales en una cadena de texto.
    """
    vocales = "aeiouAEIOU"  # Definimos las vocales en mayúsculas y minúsculas
    contador = 0  # Inicializamos el contador de vocales a 0
    for letra in cadena:  # Iteramos sobre cada letra de la cadena
        if letra in vocales:  # Verificamos si la letra es una vocal
            contador += 1  # Incrementamos el contador si la letra es una vocal
    return contador  # Retornamos el contador de vocales

# Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingresa una cadena de texto para contar las vocales: ")

# Contar el número de vocales en la cadena de texto ingresada
num_vocales = contar_vocales(texto)

# Mostrar el número de vocales en la cadena de texto
print(f"El número de vocales en la cadena de texto es: {num_vocales}")
