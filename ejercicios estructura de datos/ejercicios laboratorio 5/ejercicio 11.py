# ejercicio 11
#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
#están ordenados de menor a mayor.

def ordenar_numeros(conjunto):
    numeros_ordenados = sorted(conjunto)
    return set(numeros_ordenados)
conjunto1 = {5, 2, 4, 1, 3}
conjunto_ordenado = ordenar_numeros(conjunto1)
print(conjunto_ordenado)
