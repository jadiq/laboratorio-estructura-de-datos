#1 Crea una lista con al menos 4 nodos, duplica cada nodo de la lista
# e imprime la lista original y la listaduplicada hacia adelante y hacia atrás.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.inicio = None
        self.final = None
    
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.inicio is None:
            self.inicio = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.final
            self.final = nuevo_nodo

    def duplicar_nodos(self):
        actual = self.inicio
        while actual is not None:
            duplicado = Nodo(actual.dato)
            siguiente_original = actual.siguiente
            actual.siguiente = duplicado
            duplicado.anterior = actual
            duplicado.siguiente = siguiente_original
            if siguiente_original is not None:
                siguiente_original.anterior = duplicado
            actual = siguiente_original

    def imprimir_adelante(self):
        actual = self.inicio
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.siguiente
        print()

    def imprimir_atras(self):
        actual = self.final
        while actual is not None:
            print(actual.dato, end=" ")
            actual = actual.anterior
        print()


lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)

lista.duplicar_nodos()


print("Lista original hacia adelante:")
lista.imprimir_adelante()
print("Lista original hacia atrás:")
lista.imprimir_atras()

print("Lista duplicada hacia adelante:")
lista.imprimir_adelante()
print("Lista duplicada hacia atrás:")
lista.imprimir_atras()
