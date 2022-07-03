
from os import system

system('cls')

num1 = int(input('Informe um número:'))
num2 = int(input('Infrome outro número:'))
maior = max(num1,num2)
menor = min(num1, num2)
lista = list(range(menor, maior+1))
lista_numero_primo = []

def numero_primo(num):
    
    for i in range(2, num ):
      if num % i == 0:
        break
      else:
        lista_numero_primo.append(num)
        break
           
for i in lista:
    numero_primo(i)
   #if numero_primo(i):
     #print('ok', end='')
print('\033[32m', lista_numero_primo)    


