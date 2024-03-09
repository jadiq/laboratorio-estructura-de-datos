# ejercicio 12
#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
#están ordenados de mayor a menor.
def numeros_ordenados_de_mayor_a_menor(conjunto_numeros):

    numeros_ordenados = sorted(conjunto_numeros, reverse=True)  # Ordena los números de mayor a menor
    return set(numeros_ordenados)

# Ejemplo 
conjunto_numeros = {5, 2, 8, 1, 3}
numeros_ordenados = numeros_ordenados_de_mayor_a_menor(conjunto_numeros)
print("El conjunto de números ordenados de mayor a menor es:", numeros_ordenados)
