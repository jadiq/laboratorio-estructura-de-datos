#ejercicio 5
#Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que
#están en el primer conjunto pero no en el segundo.

def numeros_en_primer_conjunto(conjunto1, conjunto2):
    numeros_filtrados = conjunto1.difference(conjunto2)
    return numeros_filtrados

conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}
resultado = numeros_en_primer_conjunto(conjunto1, conjunto2)
print(resultado)
