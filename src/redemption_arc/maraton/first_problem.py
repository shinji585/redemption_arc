def analizar_congestion(
    numero_intersecciones: int,
    limite_de_vehiculos_por_interseccion: int,
    vehiculos_registrados: list[int],
):
    
    
    if numero_intersecciones <= 1 or numero_intersecciones >= 100000:
        raise ValueError("El numero de intersecciones por fuera de las condiciones")

    if (
        limite_de_vehiculos_por_interseccion <= 0
        or limite_de_vehiculos_por_interseccion >= 1000000000
    ):
        raise ValueError(
            "Limite de vehiculos por interseccion por fuera de las condiciones "
        )

    if len(vehiculos_registrados) <= 0 or len(vehiculos_registrados) >= 1000000000:
        raise ValueError("Numero de vehiculos por fuera de las condiciones")

    maximo = vehiculos_registrados[0]
    posicion = 1
    cantidad_intersecciones = 0
    for i, cantidad_vehiculo in enumerate(vehiculos_registrados):
        if cantidad_vehiculo > limite_de_vehiculos_por_interseccion and  cantidad_vehiculo >= maximo:
            maximo = cantidad_vehiculo
            posicion =  1 + i
            cantidad_intersecciones += 1

    return (maximo, posicion, cantidad_intersecciones)


if __name__ == "__main__":
    print(analizar_congestion(6, 100, [80, 120, 95, 120, 150, 70]))
    print(analizar_congestion(3, 50, [10,30,70]))
    print(analizar_congestion(1,10,[5]))
