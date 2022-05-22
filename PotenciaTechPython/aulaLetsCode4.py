'''--- Estruturas Condicionais ---'''

valor_passagem = 4

valor_corrida = float(input('Qual é o valor da corrida? '))

if valor_corrida <= valor_passagem*5:
    print('Pague a corrida')
elif valor_corrida <= valor_passagem*6:
    print('Espere mais um pouco')
else:
    print('Pegue um ônibus')