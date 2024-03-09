#ejercicio 1
#Escribe una función recursiva que imprima los números pares del 1 al 100.
def imprimir_pares_recursivo(numero):
    
#Función recursiva para imprimir los números pares del 1 al 100.
    
    if numero > 100:
        return  # Caso base: terminar la recursión cuando el número sea mayor que 100
    if numero % 2 == 0:
        print(numero)  # Imprimir el número par
    imprimir_pares_recursivo(numero + 1)  # Llamar recursivamente a la función con el siguiente número

# Llamar a la función para imprimir los números pares del 1 al 100 de manera recursiva
imprimir_pares_recursivo(1)
