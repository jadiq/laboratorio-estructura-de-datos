## ejercicio 6 ###
#Toma una cadena de texto y muestra su inversión

def invertir_cadena(cadena):

#Función que invierte una cadena de texto.
 
# Utilizamos slicing para invertir la cadena
    cadena_invertida = cadena[::-1]
    return cadena_invertida

# Solicitar al usuario que ingrese una cadena de texto
texto = input("Ingresa una cadena de texto para invertir: ")

# Invertir la cadena de texto ingresada
texto_invertido = invertir_cadena(texto)

# Mostrar la cadena de texto invertida
print("La cadena de texto invertida es:", texto_invertido)


