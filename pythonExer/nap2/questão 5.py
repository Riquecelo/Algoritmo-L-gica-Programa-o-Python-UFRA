'''
5) Questão
Escreva uma função que recebe uma frase como entrada e retorne o numero de vogais
presentes na frase, o seu programa deve imprimir o resultado na tela.

Equipe
- David Laurentino - 2021005218
- Lorena Maniva - 2021005076
- Marcelo Henrique dos Santos - 2016007249
- Matheus Nahum - 2021005192
- Renato Neto - 2021005307
'''
from os import system
system('cls')

frase = input('Digite a frase: ')

frase = frase.upper()
A = frase.count('A')
E = frase.count('E')
I = frase.count('I')
O = frase.count('O')
U = frase.count('U')
resultado = (A+E+I+O+U)

print(f'A frase tem {resultado} vogais')