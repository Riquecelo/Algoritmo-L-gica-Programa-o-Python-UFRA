#Teste de Condições Independentes

velocidade = float(input('Informe a velocidade:'))

if velocidade < 60:
    print('Velocidade permitida')   
if velocidade > 60 and velocidade <= 80:
    print('Acima da velocidade permitida')
if velocidade > 80:
    print('velocidade excessiva, aumentar a multa!!!')