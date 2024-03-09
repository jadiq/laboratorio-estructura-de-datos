## ejercicio 5 ###
# hazlo con comentarios en el codigo

#Función que determina si un número es primo.
#Debe recibir el número entero
def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

if primo(numero):
    print(numero, " es un número primo.")
else:
    print(numero, "no es un número primo.")
