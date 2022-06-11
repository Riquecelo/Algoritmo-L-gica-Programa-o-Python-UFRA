
print('Informe seu peso:')
peso = float(input())
print('Informe sua altura:')
altura = float(input())

imc = peso/(altura**2)
print('IMC = {:.2f}, peso ={}kg , altura ={}m'. format(imc, peso, altura))

if imc < 20:
    print('abaixo do peso ideal')
elif 20 <= imc <= 25:
    print('Peso ideal')
else:
    print('Sobrepeso')
