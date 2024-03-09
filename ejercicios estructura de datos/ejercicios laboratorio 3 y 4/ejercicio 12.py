# ejercicio 12
#Calcula la media de los elementos de una matriz.

#matriz de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calcular la media de los elementos de la matriz
suma_total = sum(sum(fila) for fila in matriz)  # Sumar todos los elementos de la matriz
total_elementos = len(matriz) * len(matriz[0])  # Calcular el número total de elementos
media = suma_total / total_elementos  # Calcular la media

# Imprimir la media de los elementos de la matriz
print("La media de los elementos de la matriz es:", media)

