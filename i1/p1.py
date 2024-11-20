x = int(input())
y = int(input())

lista = [] # lista de numeros que si estan
a = int(input())
while a != -1:
    if a <= y and a >= x:
        lista.append(a)
    
    a = int(input())

largo_lista = len(lista)
print(largo_lista)
