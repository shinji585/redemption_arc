from collections import deque
from typing import Any


def generar_matrix(fila: int, columna: int) -> list[list[Any]]:
    matrix = [["#" if j % 2 == 0 else "." for j in range(columna)] for _ in range(fila)]
    matrix[0][0] = "S"
    matrix[-1][-1] = "E"
    return matrix


def bfs_matriz(matrix: list[list[Any]]) -> list[tuple[int, int]] | int :
    filas = len(matrix)
    columnas = len(matrix[0]) if filas > 0 else 0

    inicio = (0, 0)
    for f in range(filas):
        for c in range(columnas):
            if matrix[f][c] == "S":
                inicio = (f, c)
                break

    visitados = set()
    visitados.add(inicio)
    cola = deque([inicio])

    orden_visita = []

    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while cola:
        f_actual, c_actual = cola.popleft()
        orden_visita.append((f_actual, c_actual))

        if matrix[f_actual][c_actual] == "E":
            print("¡Destino 'E' alcanzado!")

        for df, dc in movimientos:
            nueva_f, nueva_c = f_actual + df, c_actual + dc

            if 0 <= nueva_f < filas and 0 <= nueva_c < columnas and (
                matrix[nueva_f][nueva_c] != "#"
                and (nueva_f, nueva_c) not in visitados
            ):
                visitados.add((nueva_f, nueva_c))
                cola.append((nueva_f, nueva_c))

    return orden_visita if len(orden_visita) > 0 else -1


if __name__ == "__main__":
    matriz = generar_matrix(5, 6)

    print("Resultado:")
    for fila in matriz:
        print(" ".join(fila))

    print("\nResultados:")
    resultado = bfs_matriz(matriz)
    print(f"resultado en forma matrix: {resultado}")
    
    if isinstance(resultado, list):
        print(f"Numero de recorridos: {len(resultado)}")
    else: 
        print(f"No se encontro nada: {resultado}")
