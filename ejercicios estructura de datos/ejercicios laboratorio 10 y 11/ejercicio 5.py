# 5 Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el
# primero y viceversa) e imprime la lista hacia adelante y hacia atrás
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

    def invertir(self):
        actual = self.cabeza
        nueva_cola = None
        while actual:
            siguiente_nodo = actual.siguiente
            actual.siguiente = nueva_cola
            actual.anterior = siguiente_nodo
            nueva_cola = actual
            actual = siguiente_nodo
        self.cabeza = nueva_cola

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

# Crear lista enlazada con al menos 6 nodos
lista = ListaEnlazada()
datos = [1, 2, 3, 4, 5, 6]
for dato in datos:
    lista.insertar(dato, 1)

# Invertir el orden de la lista
lista.invertir()

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista.imprimir_adelante()
print("\nLista hacia atrás:")
lista.imprimir_atras()
