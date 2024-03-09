# 13 Utilizar una pila para comprobar si una palabra o frase es un palíndromo.

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

def es_palindromo(palabra):
    pila = Pila()
    palabra = palabra.lower().replace(" ", "")  # Convertir a minúsculas y eliminar espacios

    for letra in palabra:
        pila.apilar(letra)

    palabra_invertida = ""
    while not pila.esta_vacia():
        palabra_invertida += pila.desapilar()

    return palabra == palabra_invertida

# Ejemplo 
palabra = "reconocer"
if es_palindromo(palabra):
    print(f"La palabra '{palabra}' es un palíndromo")
else:
    print(f"La palabra '{palabra}' no es un palíndromo")
