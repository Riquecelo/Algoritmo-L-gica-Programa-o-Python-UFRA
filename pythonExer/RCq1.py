#Calculo IMC
#print('Descubra seu IMC, informe seus dados.')

peso = float(input('Informe seu peso:\n'))
altura = float(input('Informe sua altura:\n'))
calculaIMC = peso / (altura**2)

if calculaIMC < 20:
    print('Abaixo do peso ideal')
elif calculaIMC > 20 and calculaIMC < 25:
    print('Peso ideal')
else :
    print('Sobre peso')