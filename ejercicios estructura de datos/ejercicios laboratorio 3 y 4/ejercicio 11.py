# ejercicio 11
# Multiplica una matriz por un número.
# la matriz de ejemplo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Definir el número por el cual multiplicar la matriz
numero = 2

# Multiplicar la matriz por el número
matriz_resultante = [[elemento * numero for elemento in fila] for fila in matriz]

# Imprimir la matriz resultante
print("La matriz resultante de la multiplicación por", numero, "es:")
for fila in matriz_resultante:
    print(fila)


