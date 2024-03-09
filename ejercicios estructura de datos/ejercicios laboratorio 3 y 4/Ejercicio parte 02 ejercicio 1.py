#Ejercicio 1:
#Crea una matriz de números aleatorios de tamaño 100x100.

# Importando la biblioteca random para generar números aleatorios
import random

# Definir las dimensiones de la matriz
filas = 100
columnas = 100

# Crear la matriz de números aleatorios
matriz_aleatoria = [[random.randint(1, 100) for _ in range(columnas)] for _ in range(filas)]

# Imprimir la matriz de números aleatorios
print("Matriz de números aleatorios de tamaño 100x100:")
for fila in matriz_aleatoria:
    print(fila)
