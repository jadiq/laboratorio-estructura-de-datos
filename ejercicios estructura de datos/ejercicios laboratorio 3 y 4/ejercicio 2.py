#Ejercicio 2:
#Escribe una función recursiva que imprima la suma de los números del 1 al n.
def suma_recursiva(n):
    
#Función recursiva para calcular la suma de los números del 1 al n.
    
    if n == 1:
        return 1  # Caso base: la suma de los números del 1 al 1 es 1
    else:
        return n + suma_recursiva(n - 1)  # Llamar recursivamente a la función con n-1 y sumar el resultado a n

# Llamar a la función para imprimir la suma de los números del 1 al n de manera recursiva
n = 10  
print(f"La suma de los números del 1 al {n} es: {suma_recursiva(n)}")
