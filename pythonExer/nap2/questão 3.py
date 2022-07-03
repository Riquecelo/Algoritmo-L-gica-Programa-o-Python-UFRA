'''
3) Questão
Escreva um programa que o usuário digite um numero inteiro n qualquer, esse número deve
ser usado como argumentos de uma função que deve imprimir na tela os 'n' termos da
série de Fibonacci. Nesta série, os dois primeiros termos são 1 e os próximos são a soma dos
dois anteriores. Serie de Fibonacci: 1, 1, 2, 3, 5, 8, 13,... por exemplo se n = 8 a função deve
imprimir os 8 primeiros termos da serie de Fibonacci.

Equipe
- David Laurentino - 2021005218
- Lorena Maniva - 2021005076
- Marcelo Henrique dos Santos - 2016007249
- Matheus Nahum - 2021005192
- Renato Neto - 2021005307
'''
from os import system
system('cls')

n = int(input('digite quantos termos você quer calcular: '))

if n == 1:
    print('1')
elif n == 2:
    print('1, 1')
else:
    T1 = 1
    T2 = 1
    print('1, 1,', end=' ')
    n = n-2
    for i in range(n):
        T3 = T1 + T2
        print(f'{T3}', end=', ')
        T1, T2 = T2, T3

print()