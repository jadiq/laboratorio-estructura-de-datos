## ejercicio 15 ###
# Toma un número entero y calcula la suma de sus dígitos. 
# Solicitar al usuario que ingrese un número entero
numero = input("Ingresa un número entero: ")

# Inicializar la variable para almacenar la suma de los dígitos
suma_digitos = 0

# Iterar sobre cada dígito del número y sumarlo a la variable suma_digitos
for digito in numero:
    suma_digitos += int(digito)

# Mostrar el resultado de la suma de los dígitos
print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
