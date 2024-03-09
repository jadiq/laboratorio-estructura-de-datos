#15 Implementa una función que invierta el orden de una lista enlazada simple
# Definición de la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Definición de la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def invertir(self):
        previo = None
        actual = self.cabeza
        siguiente = None
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente
        self.cabeza = previo

    def imprimir(self):
        nodos = []
        actual = self.cabeza
        while actual:
            nodos.append(actual.dato)
            actual = actual.siguiente
        print(" -> ".join(map(str, nodos)))

# Creación de la lista enlazada y añadir nodos
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)

# Invertir el orden de la lista enlazada
lista.invertir()

# Imprimir la lista con el orden invertido
print("Lista con el orden invertido:")
lista.imprimir()
