#ejercicio 6
#Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que
#están en el segundo conjunto pero no en el primero
def numeros_en_conjunto2_no_en_conjunto1(conjunto1, conjunto2):
    
    # Utiliza la diferencia de conjuntos para encontrar los números en el segundo conjunto pero no en el primero
    numeros_diferentes = conjunto2 - conjunto1
    return numeros_diferentes

# Ejemplo 
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
diferentes = numeros_en_conjunto2_no_en_conjunto1(conjunto1, conjunto2)
print("El conjunto de números en el segundo conjunto pero no en el primero es:", diferentes)

