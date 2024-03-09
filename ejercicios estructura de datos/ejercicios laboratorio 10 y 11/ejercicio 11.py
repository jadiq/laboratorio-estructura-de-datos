# 11 Eliminar los elementos duplicados de una pila

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

def eliminar_duplicados_pila(pila):
    elementos_unicos = set()
    pila_sin_duplicados = Pila()

    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in elementos_unicos:
            elementos_unicos.add(elemento)
            pila_sin_duplicados.apilar(elemento)

    return pila_sin_duplicados

# Ejemplo 
pila_original = Pila()
elementos = [3, 5, 2, 5, 8, 3, 1, 2]
for elemento in elementos:
    pila_original.apilar(elemento)

pila_sin_duplicados = eliminar_duplicados_pila(pila_original)
print("Elementos de la pila sin duplicados:")
while not pila_sin_duplicados.esta_vacia():
    print(pila_sin_duplicados.desapilar())
