import hotel 

def obtener_habitacion(nombre):
    x = hotel.num_habitaciones()
    for indice in range (x):
        if hotel.nombre_ocupante(indice) == nombre:
            return indice
    return -1
