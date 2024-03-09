# ejercicio 9
#Accede al elemento central de una matriz.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Determinar las dimensiones de la matriz
filas = len(matriz)
columnas = len(matriz[0])  # Suponiendo que todas las filas tienen la misma longitud

# Acceder al elemento central de la matriz
if filas % 2 != 0 and columnas % 2 != 0:  # Verificar si el número de filas y columnas es impar
    elemento_central = matriz[filas // 2][columnas // 2]
    print("El elemento central de la matriz es:", elemento_central)
else:
    print("La matriz no tiene un único elemento central debido a su tamaño par.")



