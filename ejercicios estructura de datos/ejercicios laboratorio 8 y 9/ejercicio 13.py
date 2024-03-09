#13 Implementa una función que concatene dos listas enlazadas simples

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

    def concatenar(self, otra_lista):
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = otra_lista.cabeza

    def imprimir(self):
        nodos = []
        actual = self.cabeza
        while actual:
            nodos.append(actual.dato)
            actual = actual.siguiente
        print(" -> ".join(map(str, nodos)))

# Creación de las listas enlazadas y añadir nodos
lista1 = ListaEnlazada()
lista1.agregar(1)
lista1.agregar(2)
lista1.agregar(3)

lista2 = ListaEnlazada()
lista2.agregar(4)
lista2.agregar(5)

# Concatenar las listas enlazadas
lista1.concatenar(lista2)

# Imprimir la lista concatenada
print("Lista concatenada:")
lista1.imprimir()
