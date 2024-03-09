#1. Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para
#comparar los caracteres de la palabra en orden original y reverso.

from collections import deque #Importamos la clase deque del módulo collections

def es_palindromo(palabra): #Definimos la función
    cola = deque()
    for letra in palabra:
        cola.append(letra)

    es_palindromo = True
    while len(cola) > 1 and es_palindromo:#nicializamos la variable es palindromo como True
        primera_letra = cola.popleft()
        ultima_letra = cola.pop()
        if primera_letra != ultima_letra:
            es_palindromo = False

    return es_palindromo#Finalmente, devolvemos el valor

# Ejemplo de uso
palabra = "reconocer"
resultado = es_palindromo(palabra)
print(f"La palabra {palabra} es palíndroma: {resultado}")


