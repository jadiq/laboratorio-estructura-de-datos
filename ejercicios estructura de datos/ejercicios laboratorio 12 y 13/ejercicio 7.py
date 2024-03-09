# 7. Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_internos(arbol):
    if not arbol.hijos:
        return 0
    cantidad = 1
    for hijo in arbol.hijos:
        cantidad += contar_nodos_internos(hijo)
    return cantidad

# Ejemplo
# Creamos un árbol de ejemplo
raiz = Nodo(1)
hijo1 = Nodo(2)
hijo2 = Nodo(3)
hijo3 = Nodo(4)
raiz.hijos = [hijo1, hijo2, hijo3]
nieto1 = Nodo(5)
nieto2 = Nodo(6)
hijo1.hijos = [nieto1, nieto2]

# Contamos la cantidad de nodos internos en el árbol
cantidad_nodos_internos = contar_nodos_internos(raiz)
print(f"La cantidad de nodos internos en el árbol es: {cantidad_nodos_internos}")

