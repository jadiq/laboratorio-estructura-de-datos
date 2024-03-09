
#ejercicio 3
#Escriba una función que reciba un conjunto de números y
#devuelva un conjunto con los números que
#son divisibles por un número determinado.

def numeros_divisibles_en_conjunto(conjunto, divisor):
    divisibles = set()
    for numero in conjunto:
        if numero % divisor == 0:
            divisibles.add(numero)
    return divisibles
#ejemplo
conjunto_de_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 3
conjunto_divisible = numeros_divisibles_en_conjunto(conjunto_de_numeros, divisor)

print("Conjunto original:", conjunto_de_numeros)
print(f"Conjunto divisible por {divisor}:", conjunto_divisible)

