'''
Para existir um triangulo é necessário que a soma de dois lados
quaisquer (tem que testar todas as combinações possíveis) seja
maior ou igual que o outro lado. Apos esse calculo o algoritmo ainda
deve informar se o triangulo é escaleno (todos os lados diferentes),
Isósceles (dois lados iguais ) ou equilátero ( todos os lados iguais).
'''

a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))

if (a + b) >= c and (a + c) >= b and (c + b) >= a:
    # testes para tipo de triangulo
    if a == b and b == c and a == c:
        print('Triangulo equilatero')
    if a != b and b != c and a != c:
        print('Triangulo escaleno')
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print('Triangulo isoceles')
else:
    print('os valores informados não formam um triangulo')
