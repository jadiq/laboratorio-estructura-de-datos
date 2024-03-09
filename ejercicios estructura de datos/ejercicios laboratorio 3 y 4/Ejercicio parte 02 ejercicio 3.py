#Ejercicio 3:
#Escribe una función que encuentre el elemento máximo de una matriz
def encontrar_maximo(matriz):
    
    maximo = float('-inf')  # Inicializar el máximo con un valor muy pequeño
    for fila in matriz:
        for elemento in fila:
            if elemento > maximo:
                maximo = elemento
    return maximo

# Ejemplo 
matriz_ejemplo = [
    [1, 5, 3],
    [4, 8, 2],
    [7, 6, 9]
]
maximo = encontrar_maximo(matriz_ejemplo)
print("El elemento máximo de la matriz es:", maximo)



