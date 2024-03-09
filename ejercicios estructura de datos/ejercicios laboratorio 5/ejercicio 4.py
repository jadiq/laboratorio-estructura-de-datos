#ejercicio 4
#Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que
#están en ambos conjuntos
def numeros_en_comun(conjunto1, conjunto2):
    
    # Utiliza la intersección de conjuntos para encontrar los números en común
    numeros_comunes = conjunto1.intersection(conjunto2)
    return numeros_comunes

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
comunes = numeros_en_comun(conjunto1, conjunto2)
print("El conjunto de números en común es:", comunes)
