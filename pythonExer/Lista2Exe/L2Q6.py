while True:
    numDigitado = int(input('Digite um valor :'))
    if numDigitado < 0 or numDigitado > 100:
        print('Só aceita valores entre 0 e 100')
    else:
        break
lista = list(range(numDigitado))
listaPar = []
for i in lista:
    if i % 2 == 0:
        listaPar.append(i)

print(listaPar)