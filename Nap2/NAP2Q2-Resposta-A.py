''' 
NAP 2
Questão 2
Equipe
Marcelo Santos - Matrícula 2016007249
Cristian Lopes - Matrícula 2021005020
Renato Barbosa - Matrícula 2021005307
David Laurentino - Matrícula 2021005218
Matheus Nahum - Matrícula 2021005192
Lorena Maniva - Matrícula 2021005076
'''
from os import system
system('cls')

while True:
    print('''\033[34m Programa Verifica Número Primo
              Descubra quantos números primos existem dentro de um intervalo de números.
              Digite para entrar - ( 1 )
              Digite para sair   - ( 0 )\033[m
    ''')
    opcao = int(input('> : '))

    if opcao == 1:
        
        num1 = int(input('Informe um número:'))
        num2 = int(input('Infrome outro número:'))

        if type(num1) != int or type(num2) != int :
            print('\033[1;41 programa só aceita números\033[m','\n')
            continue

        maior = max(num1,num2)
        menor = min(num1, num2)
        lista = list(range(menor, maior+1))
        lista_numero_primo = []

        def numero_primo(num):
            cont = 0
            for y in range(1, num+1):
                if i % y ==0:
                    cont+=1
            if cont == 2:
                lista_numero_primo.append(num)

        for i in lista:
            numero_primo(i)

        if lista_numero_primo == []:
            print('\033[1;33mNão existe números primos nesse intervalo\033[m','\n')
        else:
            print('\033[32mOs números primos nesse intervalo são:\033[m')
            print('\033[32m', lista_numero_primo,'\033[m')    
            print('\n')

    elif opcao == 0:
        print('\033[7mFinalizando o programa...\033[m','\n')
        break
    else:
        print('\033[1;31;40m Comando inválido, tente mais uma vez!\033[m''\n')