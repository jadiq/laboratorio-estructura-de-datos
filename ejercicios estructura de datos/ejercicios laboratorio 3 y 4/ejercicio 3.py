#ejercicio 3
#Escribe una función recursiva que imprima la pirámide de números del 1 al n.

def piramide_recursiva(n):
    """
    Función recursiva para imprimir la pirámide de números del 1 al n.
    """
    if n == 0:
        return  # Caso base: terminar la recursión cuando n sea 0
    piramide_recursiva(n-1)  # Llamar recursivamente a la función con n-1
    print(" ".join(str(i) for i in range(1, n+1)))  # Imprimir los números del 1 a n en forma de pirámide

# Llamar a la función para imprimir la pirámide de números del 1 al n de manera recursiva
n = 5  # Aquí puedes cambiar el valor de n
piramide_recursiva(n)


