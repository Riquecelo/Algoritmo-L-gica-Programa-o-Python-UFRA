'''
4) Questão
Escreva uma função que receba dois números inteiros quaisquer, e que calcule a soma dos
números pares entre esses dois números, a função deve retornar esse valore e o seu
programa deve imprimir esse resultado na tela.

Equipe
- David Laurentino - 2021005218
- Lorena Maniva - 2021005076
- Marcelo Henrique dos Santos - 2016007249
- Matheus Nahum - 2021005192
- Renato Neto - 2021005307
'''
from os import system
system('cls')

n1 = int(input('Digite o Primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

maior = max(n1,n2)
menor = min(n1,n2)

soma = 0
for i in range(menor, maior + 1):
    if i % 2 == 0:
        soma = soma + i

print(f'A soma dos numeros pares entre {menor} e {maior} é {soma}')