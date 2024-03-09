# 10 Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

def ordenar_pila_ascendente(pila):
    pila_ordenada = Pila()
    while not pila.esta_vacia():
        temp = pila.desapilar()
        while not pila_ordenada.esta_vacia() and pila_ordenada.items[-1] > temp:
            pila.apilar(pila_ordenada.desapilar())
        pila_ordenada.apilar(temp)
    return pila_ordenada

# Ejemplo 
pila_original = Pila()
elementos = [5, 3, 8, 1, 2]
for elemento in elementos:
    pila_original.apilar(elemento)

pila_ordenada = ordenar_pila_ascendente(pila_original)
print("Elementos de la pila ordenados de manera ascendente:")
while not pila_ordenada.esta_vacia():
    print(pila_ordenada.desapilar())
