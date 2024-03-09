# 8. Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz
# hasta una hoja).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def altura_arbol(arbol):
    if not arbol.hijos:
        return 0
    altura_max = 0
    for hijo in arbol.hijos:
        altura_max = max(altura_max, altura_arbol(hijo))
    return 1 + altura_max

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

# Calculamos la altura del árbol
altura = altura_arbol(raiz)
print(f"La altura del árbol es: {altura}")

