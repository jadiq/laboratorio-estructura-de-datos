# ejercicio 14
#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que no
#están duplicados.
def numeros_no_duplicados(conjunto_numeros):
    
   # Encuentra los números que no están duplicados en el conjunto dado.

    numeros_no_duplicados = {numero for numero in conjunto_numeros if list(conjunto_numeros).count(numero) == 1}
    return numeros_no_duplicados

# Ejemplo 
conjunto_numeros = {1, 2, 3, 4, 3, 2, 5}
numeros_no_duplicados = numeros_no_duplicados(conjunto_numeros)
print("El conjunto de números que no están duplicados es:", numeros_no_duplicados)
