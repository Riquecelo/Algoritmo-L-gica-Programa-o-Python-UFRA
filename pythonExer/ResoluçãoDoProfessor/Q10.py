ano_nasc = int(input('Informe seu ano de nascimento:'))
idade = 2021 - ano_nasc
print(f'Você tem {idade} anos de idade')

if idade < 18:
    print('Menor de idade')
elif 18 <= idade < 50:
    print('Maior de idade')
else:
    print('Senior')
