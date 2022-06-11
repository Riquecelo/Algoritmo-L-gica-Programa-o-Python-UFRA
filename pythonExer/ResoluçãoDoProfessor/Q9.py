nap1 = float(input('Informe a nota do nap1:'))
nap2 = float(input('Informe a nota do nap2:'))
subs = float(input('Informe a nota da substitutiva:'))

menor = min(nap1, nap2, subs)

soma = nap1 + nap2 + subs - menor

media_inicial = soma/2

if media_inicial >= 6:
    print('Aprovado media final = {:.2f}'.format(media_inicial))
elif media_inicial < 4:
    print('Reprovado por media, media final={:.2f}'.format(media_inicial))
else:
    NAF = 12 - media_inicial
    print('Aluno de Recuperação')
    print('voce precisa tirar {:.2f} no NAF'.format(NAF))
