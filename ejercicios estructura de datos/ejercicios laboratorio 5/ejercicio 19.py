# ejercicio 19
#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
#están ordenados de menor a mayor y que no están duplicados.
def numeros_ordenados_sin_duplicados(conjunto):
    numeros_ordenados = sorted(set(conjunto))
    return set(numeros_ordenados)

mi_conjunto = {5, 2, 8, 1, 3, 5, 8}
resultado = numeros_ordenados_sin_duplicados(mi_conjunto)
print(resultado)
