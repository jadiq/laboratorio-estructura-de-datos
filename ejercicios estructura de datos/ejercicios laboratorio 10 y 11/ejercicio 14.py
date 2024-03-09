# 14 Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los
# deshaceres.

class SistemaDeshacer:
    def __init__(self):
        self.acciones = []
        self.deshaceres = []

    def hacer_accion(self, accion):
        self.acciones.append(accion)
        # Limpiar la pila de deshaceres al realizar una nueva acción
        self.deshaceres = []

    def deshacer_accion(self):
        if self.acciones:
            accion_deshacer = self.acciones.pop()
            self.deshaceres.append(accion_deshacer)
            print(f"Deshaciendo la acción: {accion_deshacer}")
        else:
            print("No hay acciones para deshacer")

    def rehacer_accion(self):
        if self.deshaceres:
            accion_rehacer = self.deshaceres.pop()
            self.acciones.append(accion_rehacer)
            print(f"Rehaciendo la acción: {accion_rehacer}")
        else:
            print("No hay acciones para rehacer")

# Ejemplo 
sistema = SistemaDeshacer()
sistema.hacer_accion("Editar texto")
sistema.hacer_accion("Guardar archivo")
sistema.deshacer_accion()  # Deshacer Guardar archivo
sistema.rehacer_accion()    # Rehacer Guardar archivo

