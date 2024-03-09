## ejercicio 11 ###
#Ordena una lista de números ingresados por el usuario de menor a mayor
# Solicitar al usuario que ingrese los números separados por espacios
entrada_usuario = input("Ingresa una lista de números separados por espacios: ")
# Convertir la entrada del usuario en una lista de números
lista_numeros = [float(numero) for numero in entrada_usuario.split()]
# Ordenar la lista de números de menor a mayor
lista_numeros.sort()

# Mostrar la lista de números ordenada de menor a mayor
print("Lista ordenada de menor a mayor:", lista_numeros)

