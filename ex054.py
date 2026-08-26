import datetime
contagem = 0
hoje = datetime.date.today().year
totalmaior = 0
totalmenor = 0
for c in range (1, 8):
    contagem +=1
    ano = int(input('Digite o ano de nascimento da {} pessoa: '.format(contagem,)))
    if (hoje - ano)<= 18:
        totalmenor += 1
    else:
        totalmaior += 1
print('Temos {} em maioridade'.format(totalmaior))
print('Temos {} em menorridade'.format(totalmenor))


