
# 9. Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz
# hasta el nodo).
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def profundidad_nodo(raiz, valor_busqueda, profundidad_actual=0):
    if raiz.valor == valor_busqueda:
        return profundidad_actual
    for hijo in raiz.hijos:
        profundidad = profundidad_nodo(hijo, valor_busqueda, profundidad_actual + 1)
        if profundidad:
            return profundidad
    return None

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(1)
hijo1 = Nodo(2)
hijo2 = Nodo(3)
hijo3 = Nodo(4)
raiz.hijos = [hijo1, hijo2, hijo3]
nieto1 = Nodo(5)
nieto2 = Nodo(6)
hijo1.hijos = [nieto1, nieto2]

# Calculamos la profundidad del nodo con valor 6
profundidad = profundidad_nodo(raiz, 6)
print(f"La profundidad del nodo con valor 6 es: {profundidad}")
