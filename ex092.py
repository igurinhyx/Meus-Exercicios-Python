from datetime import datetime
ficha = dict()


ficha['Nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
ficha['idade'] = datetime.now().year - nascimento
ficha['CTPS'] = int(input('Carteira de trabalho, \033[1;33m[\033[m \033[1;31m0 não tem\033[1m \033[1;33m]\033[m: '))
if ficha['CTPS'] != 0:
    ficha['Contratação'] = int(input('Ano de contratação: '))
    ficha['Salario'] = float(input('Salário: '))
    ficha['Aposentadoria'] = ficha['idade'] + ((ficha['Contratação'] +35) - datetime.now().year)
    print()
print('=='*20)
for k, v in ficha.items():
    print(f'{k}: {v}')
print('=='*20)


