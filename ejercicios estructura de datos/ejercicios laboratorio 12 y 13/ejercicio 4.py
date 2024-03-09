# 4. Implementa un sistema de gestión de tareas que permita agregar tareas, marcar tareas como
# completadas y mostrar la próxima tarea pendiente

class SistemaGestionTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append({"tarea": tarea, "completada": False})
        print(f"Tarea '{tarea}' agregada.")

    def marcar_completada(self, indice):
        if 0 <= indice < len(self.tareas):
            self.tareas[indice]["completada"] = True
            print(f"Tarea '{self.tareas[indice]['tarea']}' marcada como completada.")
        else:
            print("Índice de tarea no válido.")

    def mostrar_proxima_pendiente(self):
        for tarea in self.tareas:
            if not tarea["completada"]:
                print(f"Próxima tarea pendiente: '{tarea['tarea']}'")
                break
        else:
            print("No hay tareas pendientes.")

# Ejemplo 
sistema = SistemaGestionTareas()
sistema.agregar_tarea("Hacer la compra")
sistema.agregar_tarea("Preparar informe")
sistema.mostrar_proxima_pendiente()
sistema.marcar_completada(0)
sistema.mostrar_proxima_pendiente()
