# 10 Desarrollar el código de buscar nodo en la lista enlazada simple.
# Definición de la clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Definición de la clase ListaEnlazada
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def buscar(self, dato):
        actual = self.cabeza
        encontrado = False
        while actual and not encontrado:
            if actual.dato == dato:
                encontrado = True
            else:
                actual = actual.siguiente
        return encontrado

# Creación de la lista enlazada y añadir nodos
lista = ListaEnlazada()
nodo1 = Nodo(5)
nodo2 = Nodo(10)
nodo3 = Nodo(15)
lista.cabeza = nodo1
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

# Buscar un nodo en la lista enlazada
dato_a_buscar = 10
if lista.buscar(dato_a_buscar):
    print(f"El dato {dato_a_buscar} ha sido encontrado en la lista.")
else:
    print(f"El dato {dato_a_buscar} no ha sido encontrado en la lista.")
