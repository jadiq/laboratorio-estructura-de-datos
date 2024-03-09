# ejercicio 13
#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
#están duplicados.
def numeros_duplicados(conjunto_numeros):

    numeros_duplicados = {numero for numero in conjunto_numeros if list(conjunto_numeros).count(numero) > 1}
    return numeros_duplicados

# Ejemplo
conjunto_numeros = {1, 2, 3, 4, 3, 2, 35}
numeros_duplicados = numeros_duplicados(conjunto_numeros)
print("El conjunto de números duplicados es:", numeros_duplicados)
