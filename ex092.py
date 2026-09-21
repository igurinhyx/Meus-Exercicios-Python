from datetime import datetime
ficha = dict()

print('\033[1;36m==\033[m'*20)
ficha['Nome'] = str(input('\033[1;35mNome: \033[m'))
nascimento = int(input('\033[1;35mAno de nascimento: \033[m'))
ficha['idade'] = datetime.now().year - nascimento
ficha['CTPS'] = int(input('Carteira de trabalho, \033[1;33m[\033[m \033[1;31m0 não tem\033[1m \033[1;33m]\033[m: '))
if ficha['CTPS'] != 0:
    ficha['Contratação'] = int(input('\033[1;35mAno de contratação:\033[m '))
    ficha['Salario'] = float(input('\033[1;35mSalário:\033[m '))
    ficha['Aposentadoria'] = ficha['idade'] + ((ficha['Contratação'] +35) - datetime.now().year)
print('\033[1;36m==\033[m' * 20)
print()
print('\033[1;36m==\033[m'*20)
for k, v in ficha.items():
    print(f'\033[1m{k}: {v}\033[m')
print('\033[1;36m==\033[m'*20)


