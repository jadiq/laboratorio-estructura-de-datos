#Ejercicio 5:
#Escribe una función que encuentre la matriz de covarianza de dos matrices. 
import numpy as np

def matriz_covarianza(matriz1, matriz2):
    """
    Encuentra la matriz de covarianza entre dos matrices.

    Args:
    matriz1 (np.array): La primera matriz.
    matriz2 (np.array): La segunda matriz.

    Returns:
    np.array: La matriz de covarianza entre las dos matrices.
    """
    # Calcular la matriz de covarianza
    cov = np.cov(np.vstack((matriz1, matriz2)))

    return cov

matriz1 = np.array([[1, 2, 3], [4, 5, 6]])
matriz2 = np.array([[6, 5, 4], [3, 2, 1]])

mat_cov = matriz_covarianza(matriz1, matriz2)
print("La matriz de covarianza entre las dos matrices es:")
print(mat_cov)
