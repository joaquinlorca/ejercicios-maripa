import hotel

def se_puede_excursion(cantidad):
    timidos = 0
    extrovertidos = 0
    for i in range(hotel.num_habitaciones()):
        perro = hotel.nombre_ocupante(i)
        caracter = hotel.obtener_caracter(perro)
        if caracter == "timido":
            timidos += 1
        elif caracter == "extrovertido":
            extrovertidos += 1

    cant_buses_timidos = cant_buses(timidos, 0)
    cant_buses_extrovertidos = cant_buses(extrovertidos, 0)
    total_buses_necesarios = cant_buses_extrovertidos + cant_buses_timidos

    if total_buses_necesarios <= cantidad:
        print(f"Suficientes: se tienen {cantidad} y se necesitan {total_buses_necesarios}")
    else:
        print(f"Insuficientes: se tienen {cantidad} y se necesitan {total_buses_necesarios}")


def cant_buses(cant_caracter, buses):
    if cant_caracter > 5:
        buses += 1
        cant_caracter -= 5
        return cant_buses(cant_caracter, buses)
    if cant_caracter <= 5 and cant_caracter != 0:
        buses += 1
    return buses
    