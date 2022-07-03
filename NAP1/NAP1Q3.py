from os import system
system('cls')

while True:

    print('''Algoritmo verifica idade
            1 - para verificar
            2 - para sair
    ''')
    opcao = int(input('>:'))

    if opcao == 1:
        dataNascimento = int(input('informe sua data de nascimento \n:'))
        idade= 2022 - dataNascimento

        if idade < 18:
            print('menor de idade\n')
            
        elif idade >= 18 and idade <= 50:
            print('maior de idade\n')
            
        else:
            print('Sênior\n')
            
        print('Ainda deseja verificar sua idade?')
    elif opcao == 2:
         print('obrigado, até a próxima!')
         break
    else:
       print('Comando inválido! Tente novamente.\n')