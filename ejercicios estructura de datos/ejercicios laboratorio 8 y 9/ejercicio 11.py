#11 Implementa una función que sume todos los nodos de una lista enlazada simple
# Definición de la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Definición de la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def sumar_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.dato
            actual = actual.siguiente
        return suma

# Creación de la lista enlazada y añadir nodos
lista = ListaEnlazada()
nodo1 = Nodo(5)
nodo2 = Nodo(10)
nodo3 = Nodo(15)
lista.cabeza = nodo1
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Sumar los nodos de la lista enlazada
resultado = lista.sumar_nodos()
print(f"La suma de los nodos de la lista enlazada es: {resultado}")
