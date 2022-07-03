''' NAP 1
Questão 4
Equipe
Marcelo Santos - Matrícula 2016007249
Cristian Lopes - Matrícula 2021005020
Renato Barbosa - Matrícula 2021005307
David laurentino - Matrícula 2021005218
Matheus Nahum - Matrícula 2021005192
Lorena Maniva - Matrícula 2021005076
'''
from os import system
system('cls')
while True:
   print('''Programa Soma dos Números
          Para entrar digite - 1
          Para sair digite   - 2 ''') 

   opcao = int(input('> :'))

   if  opcao == 1:
  
     num = int( input("Digite um número: "))
     if num <= 0 or num > 100:
          print("O programa só aceita números entre 1 e 100")
          continue
     lista = list(range(num +1))
     print(sum(lista))
   elif opcao == 2:
     print('até a proxima!')
     break
   else:
     print('comando inválido, tente novamente!')
