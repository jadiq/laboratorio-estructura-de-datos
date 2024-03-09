## ejercicio 7 ###
#Calcula la suma de los números pares en un rango especificado por el usuario.
# Solicitar al usuario que ingrese el rango
inicio = int(input("Ingresa el número inicial del rango: "))
fin = int(input("Ingresa el número final del rango: "))

# Inicializar la variable para almacenar la suma de los números pares
suma_pares = 0

# Calcular la suma de los números pares en el rango especificado
for numero in range(inicio, fin + 1):
    if numero % 2 == 0:
        suma_pares += numero

# Mostrar la suma de los números pares en el rango
print(f"La suma de los números pares en el rango de {inicio} a {fin} es: {suma_pares}")

