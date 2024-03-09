#3. Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola
#para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino.
from collections import deque

def bfs_laberinto(laberinto, inicio, destino):
    # Definir las direcciones arriba, abajo, izquierda y derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Crear una cola para el recorrido en anchura
    cola = deque([inicio])

    # Crear un conjunto para almacenar las celdas visitadas
    visitado = set(inicio)

    # Crear un diccionario para almacenar los padres de cada celda
    padres = {inicio: None}

    while cola:
        celda_actual = cola.popleft()
        if celda_actual == destino:
            break

        for direccion in direcciones:
            nueva_celda = (celda_actual[0] + direccion[0], celda_actual[1] + direccion[1])
            if nueva_celda in visitado or laberinto[nueva_celda[0]][nueva_celda[1]] == '#':
                continue
            visitado.add(nueva_celda)
            padres[nueva_celda] = celda_actual
            cola.append(nueva_celda)

    # Reconstruir el camino más corto
    camino = []
    celda = destino
    while celda:
        camino.append(celda)
        celda = padres[celda]
    camino.reverse()

    return camino

# Ejemplo
laberinto = [
    ['#', '#', '#', '#', '#', '#'],
    ['#', 'S', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', 'E', '#'],
    ['#', '#', '#', '#', '#', '#']
]

inicio = (1, 1)
destino = (4, 4)
camino_mas_corto = bfs_laberinto(laberinto, inicio, destino)
print(f"El camino más corto es: {camino_mas_corto}")

