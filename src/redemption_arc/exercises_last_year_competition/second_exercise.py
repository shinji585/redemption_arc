import pprint
import random
from typing import Any


def solicitar_datos() -> str:
    print("---------- Bienvenido a la busqueda del tesoro -----------")
    print(
        "Acontinuacion se le solicitaran las coordenadas que debera ingresarlas de la forma '2,3'"
    )
    print("Cualquier valor contrario a este formato sera rechazado")
    return input("Ingrese las coordenadas: ")


def generar_matrix() -> list[list[Any]]:
    i, j = (5, 5)
    random_positions = [random.randint(0, (i * j) - 1) for _ in range(i * j)]
    limits = {"m": 2, "o": 2}
    counts = {"v": 0, "m": 0, "o": 0}

    return [
        [
            "m"
            if (r * j + c) in random_positions
            and counts["m"] < limits["m"]
            and not counts.update({"m": counts["m"] + 1})
            else "o"
            if (r * j + c) in random_positions
            and counts["o"] < limits["o"]
            and not counts.update({"o": counts["o"] + 1})
            else "v"
            for c in range(j)
        ]
        for r in range(i)
    ]


def game():
    oro_number = 0
    matrix = generar_matrix()
    coordenada1 = 0
    coordenada2 = 0
    coordenadas_visitadas = set()

    while True:
        pprint.pprint(matrix)
        coordenadas = solicitar_datos()

        def es_coordenada(texto: str) -> bool:
            partes = texto.split(",")
            if len(partes) != 2:
                return False
            try:
                int(partes[0].strip())
                int(partes[1].strip())
                return True
            except ValueError:
                return False

        if es_coordenada(coordenadas):
            coordenada1, coordenada2 = map(int, coordenadas.split(","))
            
            if (coordenada1, coordenada2) in coordenadas_visitadas:
                print(" Ya visitaste esa casilla. \nIntenta de nuevo")
                continue

            if matrix[coordenada1][coordenada2] == "o":
                print("¡Encontraste un Oro!")
                oro_number += 1
                if oro_number == 2:
                    print("¡Felicidades! ¡Encontraste los 2 oros! ¡Ganaste!")
                    break
                coordenadas_visitadas.add((coordenada1, coordenada2))
                continue
            elif matrix[coordenada1][coordenada2] == "m":
                print("Ups ¡EEncontraste una Mina! ¡Perdiste!")
                break
            else:
                print("Casilla Vacía. Sigue jugando.")
                coordenadas_visitadas.add((coordenada1, coordenada2))
                continue


if __name__ == "__main__":
    game()
