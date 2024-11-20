import diccionario

def corregir(palabra, posicion):
    vocales = ["a", "e", "i", "o", "u"]
    for i in range(len(vocales)):
        palabra_nueva = cambiar_letra(vocales[i], palabra, posicion)
        if diccionario.valida(palabra_nueva):
            return palabra_nueva
    return palabra


def cambiar_letra(vocal, palabra, posicion):
    palabra_nueva = ""
    for i in range(len(palabra)):
        if i == posicion:
            palabra_nueva += vocal
        else:
            palabra_nueva += palabra[i]
    return palabra_nueva