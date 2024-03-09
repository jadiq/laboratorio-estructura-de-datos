# ejercicio 1
#Escriba una función que reciba un conjunto de números y
#devuelva un conjunto con los números primos.


def numeros_primos(conjunto):
    primos = set()

    def es_primo(numero):
        if numero < 2:#condicion a validar
            return False
        for i in range(2, int(numero ** 0.5) + 1):#rango a recorer
            if numero % i == 0:
                return False
        return True

    for numero in conjunto:#rango a recorer
        if es_primo(numero):
            primos.add(numero)

    return primos
#ejemplo
conjunto1 = {2, 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
primos1 = numeros_primos(conjunto1)
print(primos1)
