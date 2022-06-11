while True:
    x = int(input('Digite um número:'))
    y = int(input('Digite outro número:'))
    if x <= 0 and y <= 0:
        print('Informe números inteiros positivos.')
    else:
        break
maior = max(x,y)
menor = min(x,y)

lista = list(range(menor, maior+1))
soma = sum(lista)

print(f'A soma entre os números {menor} e {maior} é igual a {soma}')