'''
#entradas
4 valores (float ou int)

#processamentos
calcular: maior, menor, some, média aritimética

#saídas
valores
'''
print('Digit 4 valores')
a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
d = float(input('d:'))

'''
if a > b and a > c and a > d:
    print(f'{a} é o maior número')
if b > a and b > c and b > d:
    print(f'{b} é o maior número')
if c > a and c > b and c > d:
    print(f'{c} é o maior número')
if d > b and d > c and d > a:
    print(f'{d} é o maior número')    
'''

maior = max(a,b,c,d)
print(f'O maior numero = {maior}')
menor = min(a,b,c,d)
print(f'O menor numero = {menor}')
soma = a+b+c+d
print(f'A soma dos numeros = {soma}')
print(f'A media é {soma/4}')