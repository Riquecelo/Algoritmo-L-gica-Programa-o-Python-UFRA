#Teste de Condições Encadeadas

velocidade = float(input('Informe a velocidade:'))

if velocidade < 60:
    print('Velocidade permitida')   
elif velocidade > 60 and velocidade <= 80:
    print('Acima da velocidade permitida')
else:
    print('velocidade excessiva, aumentar a multa!!!')