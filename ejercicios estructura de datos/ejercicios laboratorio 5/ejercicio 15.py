# ejercicio 15
#Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
#son primos y están ordenados de menor a mayor.
def numeros_primos_ordenados(conjunto_numeros):
   
    #Devuelve un conjunto con los números primos ordenados de menor a mayor.
    def es_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                return False
        return True

    primos_ordenados = {numero for numero in conjunto_numeros if es_primo(numero)}
    primos_ordenados = sorted(primos_ordenados)  # Ordena los números primos de menor a mayor
    return set(primos_ordenados)

# Ejemplo 
conjunto_numeros = {2, 5, 8, 11, 13, 15}
numeros_primos_ordenados = numeros_primos_ordenados(conjunto_numeros)
print("El conjunto de números primos ordenados de menor a mayor es:", numeros_primos_ordenados)
