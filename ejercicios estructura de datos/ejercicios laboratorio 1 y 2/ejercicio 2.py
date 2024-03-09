#ejercicio 2:
#Solicita un número al usuario y determina si es par o impar.

# Solicitar al usuario que ingrese un número
numero = int(input("ingresa un numero: "))
# Determinar si el número es par o impar
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")
