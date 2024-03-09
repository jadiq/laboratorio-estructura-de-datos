# 4 Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando
# solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        if posicion == 1:
            nuevo_nodo.siguiente = self.cabeza
            if self.cabeza:
                self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            if self.cola is None:
                self.cola = nuevo_nodo
            return
        actual = self.cabeza
        for _ in range(1, posicion - 1):
            if actual is not None:
                actual = actual.siguiente
            else:
                break
        if actual is None:
            return
        nuevo_nodo.siguiente = actual.siguiente
        nuevo_nodo.anterior = actual
        if actual.siguiente is not None:
            actual.siguiente.anterior = nuevo_nodo
        actual.siguiente = nuevo_nodo
        if nuevo_nodo.siguiente is None:
            self.cola = nuevo_nodo

    def eliminar_duplicados(self):
        datos_vistos = set()
        actual = self.cabeza
        while actual:
            if actual.dato in datos_vistos:
                siguiente_nodo = actual.siguiente
                self.eliminar_nodo(actual)
                actual = siguiente_nodo
            else:
                datos_vistos.add(actual.dato)
                actual = actual.siguiente

    def eliminar_nodo(self, nodo):
        if nodo.anterior:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.cabeza = nodo.siguiente
        if nodo.siguiente:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self.cola = nodo.anterior

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.dato)
            actual = actual.siguiente

    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.dato)
            actual = actual.anterior

# Crear lista enlazada con datos duplicados
lista = ListaEnlazada()
datos = [1, 2, 3, 4, 2, 5, 3, 6, 1]
for dato in datos:
    lista.insertar(dato, 1)

# Eliminar nodos duplicados
lista.eliminar_duplicados()

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista.imprimir_adelante()
print("\nLista hacia atrás:")
lista.imprimir_atras()
