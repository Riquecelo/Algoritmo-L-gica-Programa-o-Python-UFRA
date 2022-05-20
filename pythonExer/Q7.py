print('Digite os lados do triângulo:')
a = float(input('lado a:'))
b = float(input('lado b:'))
c = float(input('lado c:'))

if (a + b) >= c and (a + c) >= b and (b + c) >= a:
    print('forma triangulo')
    if a != b and a != c and b != c:
        print('triangulo é escaleno')
    if (a == b and a != c) or (a == c and a != b) or (b == c and b !=a):
        print('é isoceles')
    if a == b and a == c:
        print('é equilátero')
else:
    print('não forma trinagulo')
