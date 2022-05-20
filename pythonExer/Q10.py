ano_nascimento = int(input('Digite seu ano de nascimento:'))

idade = 2022 - ano_nascimento
print(f'Sua idade é {idade}')

if idade < 18 :
    print('menor de idade')
elif idade >= 18 and idade < 50:
    print('maior de idade')
else:
    print('Sênior')