#ejercicio 4:
#Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n.


def piramide_invertida_recursiva(n):
    
#Función recursiva para imprimir la pirámide de números invertidos del 1 al n.
    
    if n == 0:
        return  # Caso base: terminar la recursión cuando n sea 0
    print(" ".join(str(i) for i in range(n, 0, -1)))  # Imprimir los números del n al 1 en forma de pirámide invertida
    piramide_invertida_recursiva(n-1)  # Llamar recursivamente a la función con n-1

# Llamar a la función para imprimir la pirámide de números invertidos del 1 al n de manera recursiva
n = 5  # Aquí puedes cambiar el valor de n
piramide_invertida_recursiva(n)



