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
  
     num = int( input("Digite um número: "))
     if num <= 0 or num > 100:
          print("O programa só aceita números entre 1 e 100")
     else:
        break
lista = list(range(num +1))
print(sum(lista))
     
 