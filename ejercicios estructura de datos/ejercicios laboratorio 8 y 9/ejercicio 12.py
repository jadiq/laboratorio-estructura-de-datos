#12 Crea una función que devuelva la longitud de una lista enlazada simple

# Definición de la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Definición de la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def longitud(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

# Creación de la lista enlazada y añadir nodos
lista = ListaEnlazada()
nodo1 = Nodo(5)
nodo2 = Nodo(10)
nodo3 = Nodo(15)
lista.cabeza = nodo1
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Obtener la longitud de la lista enlazada
longitud = lista.longitud()
print(f"La longitud de la lista enlazada es: {longitud}")


