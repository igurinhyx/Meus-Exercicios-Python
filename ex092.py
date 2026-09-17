from datetime import datetime
ficha = dict()

while True:
    ficha['Nome'] = str(input('Nome: '))
    nascimento = int(input('Digite seu ano de nascimento: '))
    ficha['idade'] = datetime.now().year - nascimento
    ficha['CTPS'] = int(input('Carteira de trabalho, \033[1;33m[\033[m \033[1;31m0 não tem\033[1m \033[1;33m]\033[m: '))
    if ficha['CTPS'] == 0:
        break
    else:
        ficha['Ano de contratacao'] = int(input('Ano de contratação: '))
        ficha['Salario'] = float(input('Salário: '))
        print()
        escolha = str(input('Digite [F] para finalizar: ')).strip().upper()[0]
        if escolha == 'F':
            break



