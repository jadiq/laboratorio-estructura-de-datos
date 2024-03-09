# 11. Implementar una función que encuentre el nodo con el valor máximo en el árbol.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_maximo(raiz):
    if raiz is None:
        return float('-inf')  # Devolver menos infinito si el nodo es nulo
    max_valor = raiz.valor
    for hijo in raiz.hijos:
        max_valor = max(max_valor, encontrar_maximo(hijo))
    return max_valor

# Ejemplo 
# Creamos un árbol de ejemplo
raiz = Nodo(10)
hijo1 = Nodo(5)
hijo2 = Nodo(8)
hijo3 = Nodo(15)
raiz.hijos = [hijo1, hijo2, hijo3]
nieto1 = Nodo(12)
nieto2 = Nodo(17)
hijo3.hijos = [nieto1, nieto2]

# Encontramos el nodo con el valor máximo en el árbol
max_valor = encontrar_maximo(raiz)
print(f"El valor máximo en el árbol es: {max_valor}")

