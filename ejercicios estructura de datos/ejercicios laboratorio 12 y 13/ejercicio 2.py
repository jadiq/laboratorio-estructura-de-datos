#2. Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que
#fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado
#actual de la cola.

from collections import deque#Importamos la clase deque del módulo collections para utilizar una cola doble.

class SistemaGestionPedidos:
    def __init__(self):#creamos la clase SistemaGestionPedidos
        self.cola_pedidos = deque()

    def agregar_pedido(self, pedido):#Agrega un pedido a la cola 
        self.cola_pedidos.append(pedido)
        print(f"Pedido {pedido} agregado a la cola.")

    def procesar_pedido(self):#Agrega un pedido a la cola 
        if self.cola_pedidos:
            pedido = self.cola_pedidos.popleft()
            print(f"Procesando pedido {pedido}.")
        else:
            print("No hay pedidos en la cola para procesar.")

    def mostrar_estado_cola(self):#Muestra el estado actual de la cola de pedidos
        print("Estado actual de la cola de pedidos:")
        print(list(self.cola_pedidos))

# Ejemplo
sistema = SistemaGestionPedidos()
sistema.agregar_pedido("Pedido 1")
sistema.agregar_pedido("Pedido 2")
sistema.mostrar_estado_cola()
sistema.procesar_pedido()
sistema.mostrar_estado_cola()
sistema.procesar_pedido()
sistema.mostrar_estado_cola()
