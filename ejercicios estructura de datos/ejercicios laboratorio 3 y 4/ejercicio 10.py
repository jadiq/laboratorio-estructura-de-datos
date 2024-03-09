# ejercicio 10
# Suma dos matrices de diferentes tamaños

# matrices de ejemplo
matriz1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]

# Verificar las dimensiones de las matrices
filas_matriz1 = len(matriz1)
columnas_matriz1 = len(matriz1[0])
filas_matriz2 = len(matriz2)
columnas_matriz2 = len(matriz2[0])

# Sumar las matrices si tienen las mismas dimensiones
if filas_matriz1 == filas_matriz2 and columnas_matriz1 == columnas_matriz2:
    matriz_resultante = [[0 for _ in range(columnas_matriz1)] for _ in range(filas_matriz1)]
    for i in range(filas_matriz1):
        for j in range(columnas_matriz1):
            matriz_resultante[i][j] = matriz1[i][j] + matriz2[i][j]
    print("La matriz resultante de la suma es:")
    for fila in matriz_resultante:
        print(fila)
else:
    print("La suma de matrices no es posible debido a sus dimensiones diferentes.")


