a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
d = float(input('d:'))

# teste para maior numero
if a > b and a > c and a > d:
    print(f'maior numero ={a}')

if b > a and b > c and b > d:
    print(f'maior numero ={b}')

if c > a and c > b and c > d:
    print(f'maior numero ={c}')

if d > a and d > b and d > c:
    print(f'maior numero ={d}')


# teste para menor numero
if a < b and a < c and a < d:
    print(f'menor numero ={a}')

if b < a and b < c and b < d:
    print(f'menor numero ={b}')

if c < a and c < b and c < d:
    print(f'menor numero ={c}')

if d < a and d < b and d < c:
    print(f'menor numero ={d}')

soma = a + b + c + d
print(f'Soma dos numeros ={soma}')

media = soma/4
print(f'Media aritmetica ={media}')
