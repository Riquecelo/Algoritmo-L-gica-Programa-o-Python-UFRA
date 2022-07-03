from os import system
system('cls')

while True:
    num1 = int(input("Digite um número :"))
    num2 = int(input("Digite outro numero :"))
    if (num1 <= 0 or num1 >100) or (num2 <=0 or num2 > 100):
        print('não está bom')
    else:
        print('Agora sim!')
        break
menor = min(num1, num2)
maior = max(num1, num2)
listaInit = list(range(menor, maior +1))
print(listaInit)

listaPar = []
listaImpar= []

for i in listaInit:
    if i % 2 == 0:
        listaPar.append(i)
    if i % 2 != 0:
        listaImpar.append(i)
print(f'A soma dos pares  {sum(listaPar)}')
print(f'A soma dos impares  {sum(listaImpar)}')