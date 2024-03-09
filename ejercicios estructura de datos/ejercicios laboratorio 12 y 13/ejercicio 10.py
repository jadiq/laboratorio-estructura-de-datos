# 10. Implementar una función que encuentre el nodo con el valor mínimo en el árbol.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_minimo(raiz):
    if raiz is None:
        return float('inf')  # Devolver infinito si el nodo es nulo
    min_valor = raiz.valor
    for hijo in raiz.hijos:
        min_valor = min(min_valor, encontrar_minimo(hijo))
    return min_valor

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(10)
hijo1 = Nodo(5)
hijo2 = Nodo(8)
hijo3 = Nodo(3)
raiz.hijos = [hijo1, hijo2, hijo3]
nieto1 = Nodo(12)
nieto2 = Nodo(7)
hijo1.hijos = [nieto1, nieto2]

# Encontramos el nodo con el valor mínimo en el árbol
min_valor = encontrar_minimo(raiz)
print(f"El valor mínimo en el árbol es: {min_valor}")

