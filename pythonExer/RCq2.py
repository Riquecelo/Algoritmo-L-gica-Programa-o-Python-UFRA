nasc = int(input('Informe o ano do seu nascimento:\n'))

idade = 2022 - nasc

if idade < 18:
    print('Menor de idade')
elif idade >18 and idade < 50:
    print('Maior de idade')
else:
    print('Sênior')