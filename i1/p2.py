lista = []

a = int(input())
while a != -1:
    lista.append(a)
    a = int(input())


def borrar_lista(lista):
    for i in range(len(lista)):
        lista.pop()


def funcion(lista, racha, contador_rachas, contador_racha):
    for i in lista:
        if len(racha) == 0:
            racha.append(i)
            contador_racha += 1

        if i <= racha[-1]:
            borrar_lista(racha)
            contador_racha = 1
            racha.append(i)

        if i != racha[-1] and i > racha[-1]:
            racha.append(i)
            contador_racha += 1



        if contador_racha == 3:
            contador_rachas += 1
            contador_racha = 2
            racha.pop(0)
    print(contador_rachas)


contador_rachas = 0
racha = []
contador_racha = 0
funcion(lista, racha, contador_rachas, contador_racha)