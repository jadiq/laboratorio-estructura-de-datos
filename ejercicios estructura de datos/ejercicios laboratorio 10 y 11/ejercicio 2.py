#2 Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato
#par y cuántos tienen un dato impar e imprime la lista hacia adelante y hacia atrás
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

    def contar_pares_impares(self):
        actual = self.inicio
        pares = 0
        impares = 0
        while actual is not None:
            if actual.dato % 2 == 0:
                pares += 1
            else:
                impares += 1
            actual = actual.siguiente
        return pares, impares

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
for i in range(1, 10):
    lista.agregar(i)

pares, impares = lista.contar_pares_impares()
print(f"Nodos pares: {pares}, Nodos impares: {impares}")
print("Lista hacia adelante:")
lista.imprimir_adelante()
print("Lista hacia atrás:")
lista.imprimir_atras()
