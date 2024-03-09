#ejercico 5
#Escribe una función recursiva que imprima la tabla de multiplicar del n.

def tabla_multiplicar_recursiva(tabla, numVeces):
    
#Función recursiva para imprimir la tabla de multiplicar correspondiente de forma recursiva.
    
    if numVeces > 1:
        tabla_multiplicar_recursiva(tabla, numVeces - 1)  # Llamar recursivamente a la función con numVeces-1
    print(f"{tabla} x {numVeces} = {tabla * numVeces}")  # Imprimir la línea de la tabla de multiplicación

# Llamar a la función para imprimir la tabla de multiplicar de forma recursiva
tabla = 5  # Aquí puedes cambiar el valor de la tabla
numVeces = 10  # Aquí puedes cambiar el número de multiplicadores a mostrar
tabla_multiplicar_recursiva(tabla, numVeces)



