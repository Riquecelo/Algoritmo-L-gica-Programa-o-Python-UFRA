'''
1) Questão
Escreva um programa que tenha uma função que receba como argumento o valor dos dois
catetos de um triangulo retângulo e a função retorne o valor da hipotenusa, imprima o
resultado na tela.

Equipe
- David Laurentino - 2021005218
- Lorena Maniva - 2021005076
- Marcelo Henrique dos Santos - 2016007249
- Matheus Nahum - 2021005192
- Renato Neto - 2021005307
'''
from os import system
system('cls')

cad = int(input('Digite o valor do cateto adjacente: '))
cop = int(input('Digite o valor do cateto oposto: '))

hip = (cad**2) + (cop**2)

print(f'O valor da hipotenusa é {hip}')