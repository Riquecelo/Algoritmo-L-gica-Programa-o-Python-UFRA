#Calculo IMC
print('Descubra seu IMC, informe seus dados.')
altura = float(input('Digite sua altura:'))
peso = float(input('Digite seu peso:'))
calculaIMC = peso / (altura**2)
print(f'Seu IMC é {calculaIMC}')

if calculaIMC < 20:
    print('Seu IMC está abaixo do ideal.')
if calculaIMC > 20 and calculaIMC < 25:
    print('Seu IMC está no peso ideal.')
if calculaIMC > 25:
    print('Seu IMC está acima do ideal, sobre peso.')