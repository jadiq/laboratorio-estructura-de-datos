#Ejercicio 4:
#Escribe una función que encuentre la submatriz de mayor suma de una matriz.
def encontrar_submatriz_mayor_suma(matriz):
    
    filas = len(matriz)
    columnas = len(matriz[0])
    max_suma = float('-inf')
    submatriz = []

    # Algoritmo para encontrar la submatriz de mayor suma
    for i in range(filas):
        for j in range(columnas):
            for k in range(i, filas):
                for l in range(j, columnas):
                    suma_actual = sum(sum(matriz[x][j:l+1]) for x in range(i, k+1))
                    if suma_actual > max_suma:
                        max_suma = suma_actual
                        submatriz = [fila[j:l+1] for fila in matriz[i:k+1]]

    return submatriz


matriz_ejemplo = [
    [1, 2, -1, -4, -20],
    [-8, -3, 4, 2, 1],
    [3, 8, 10, 1, 3],
    [-4, -1, 1, 7, -6]
]
submatriz_mayor_suma = encontrar_submatriz_mayor_suma(matriz_ejemplo)
print("La submatriz de mayor suma es:")
for fila in submatriz_mayor_suma:
    print(fila)
