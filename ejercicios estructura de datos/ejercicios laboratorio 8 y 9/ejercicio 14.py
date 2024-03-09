#14 Crea una función que elimine los nodos duplicados de una lista enlazada simple.

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

    def eliminar_duplicados(self):
        valores_vistos = set()
        actual = self.cabeza
        previo = None
        while actual:
            if actual.dato in valores_vistos:
                previo.siguiente = actual.siguiente
            else:
                valores_vistos.add(actual.dato)
                previo = actual
            actual = actual.siguiente

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
lista.agregar(2)
lista.agregar(4)
lista.agregar(1)

# Eliminar nodos duplicados
lista.eliminar_duplicados()

# Imprimir la lista sin nodos duplicados
print("Lista sin nodos duplicados:")
lista.imprimir()
