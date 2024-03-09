### ejercicio 4 ###
#Crea una función que calcule la factorial de un número.

def factorial(numero):
    """
    numero: El número del cual se quiere calcular el factorial.
    Retorna: El factorial del número.
    """
# condiciones a cumplir
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

# Pedir al usuario que ingrese un número
num = int(input("Ingresa un número para calcular su factorial: "))

# Calcular el factorial del número ingresado
resultado = factorial(num)

# Mostrar el resultado
print("El factorial de", num, "es", resultado)
