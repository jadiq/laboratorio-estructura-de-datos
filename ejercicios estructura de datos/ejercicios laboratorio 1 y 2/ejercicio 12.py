## ejercicio 12 ###
#Verifica si una palabra ingresada por el usuario es un palíndromo.
# Solicitar al usuario que ingrese una palabra para verificar si es un palíndromo
palabra = input("Ingresa una palabra: ")
# Verificar si la palabra es igual a su reverso
if palabra == palabra[::-1]:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")

