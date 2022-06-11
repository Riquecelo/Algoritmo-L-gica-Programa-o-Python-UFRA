from random import randint
lista =[]
for i in range(50):
    x = randint(1, 10)
    lista.append(x)

for e,valor in enumerate(lista):
    print(e ,'-', valor)
