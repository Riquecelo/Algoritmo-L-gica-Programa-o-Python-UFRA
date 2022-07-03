''' NAP 2
Questão 2
Equipe
Marcelo Santos - Matrícula 2016007249
Cristian Lopes - Matrícula 2021005020
Renato Barbosa - Matrícula 2021005307
David Laurentino - Matrícula 2021005218
Matheus Nahum - Matrícula 2021005192
Lorena Maniva - Matrícula 2021005076

from os import system
system('cls')

num1 = int(input('Informe um número:'))
num2 = int(input('Infrome outro número:'))


def numero_primo(num1, num2):
    maior = max(num1,num2)
    menor = min(num1, num2)
    numeros_primos =[]
    lista = list(range(menor, maior+1))

    for i in lista:
        for c in range(1, maior+1):
            cont= 0
            if i%2==0: 
                print('\033[32m',end=' ')
                cont +=1
            if cont >= 3:
                numero_primo.append(i)
    print(numero_primo)                
#print('{} '.format(numero_primo),end='')


print(numero_primo(num1, num2))

#------------------------------
from os import system
system('cls')
num1 = int(input('Informe um número:'))
num2 = int(input('Infrome outro número:'))
maior = max(num1,num2)
menor = min(num1, num2)

def primo(numero):
    if numero ==1:
        return False
    for n in range(numero - 1, 1, -1):
        if numero % n == 0:
            return False
        return True

print(f'numeros primos entre {menor} e {maior}')
for n in range(menor, maior +1):
    if primo(n):
        print(n, end=' ')'''

#-------------------------------------

from inspect import _void
from os import system
system('cls')
num1 = int(input('Informe um número:'))
num2 = int(input('Infrome outro número:'))
maior = max(num1,num2)
menor = min(num1, num2)

def primo(numero):
    divisor = 0
    for n in range(1, numero+1):
        if numero % n == 0:
            divisor +=1
        if divisor == 2:
            return numero
        else:
            return False
    

print(f'numeros primos entre {menor} e {maior}')
for n in range(menor, maior +1):
    if primo(n):
        print(n, end=' ')