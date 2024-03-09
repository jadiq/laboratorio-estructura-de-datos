## ejercicio 10 ###
#Genera los primeros 10 números de la serie Fibonacci.
# Inicializar los dos primeros números de la serie Fibonacci
a, b = 0, 1

# Crear una lista para almacenar los números de la serie Fibonacci
fibonacci = [a, b]

# Generar los siguientes 8 números de la serie Fibonacci
for _ in range(8):
    # Calcular el siguiente número de la serie Fibonacci
    a, b = b, a + b
    # Agregar el siguiente número a la lista
    fibonacci.append(b)

# Mostrar la lista de los primeros 10 números de la serie Fibonacci
print("Los primeros 10 números de la serie Fibonacci son:", fibonacci)



