## ejercicio 13 ###
#Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario. 
# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número para generar su tabla de multiplicar: "))

# Generar la tabla de multiplicar del número ingresado
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):  # Iterar sobre los números del 1 al 10
    resultado = numero * i  # Calcular el resultado de la multiplicación
    print(f"{numero} x {i} = {resultado}")  # Mostrar la operación y el resultado
