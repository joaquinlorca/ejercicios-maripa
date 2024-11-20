import diccionario

def corregir_2(palabra, p1, p2):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    
    for j in range(len(abecedario)):
        palabra_nueva = cambiar_letra(abecedario[j], palabra, p1)
        for i in range(len(abecedario)):
            palabra_nueva = cambiar_letra(abecedario[i], palabra_nueva, p2)
            if diccionario.valida(palabra_nueva):
                return palabra_nueva
    return palabra


def cambiar_letra(letra, palabra, posicion):
    palabra_nueva = ""
    for i in range(len(palabra)):
        if i == posicion:
            palabra_nueva += letra
        else:
            palabra_nueva += palabra[i]
    return palabra_nueva