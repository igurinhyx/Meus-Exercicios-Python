import datetime
ficha = dict()

anoatual = datetime.date.today().year

while True:
    ficha['Nome'] = str(input('Nome: '))
    ficha['Ano de nascimento'] = int(input('Ano de nascimento: '))
    ficha['CTPS'] = int(input('Carteira de trabalho [ 0 não tem ]: '))
    if ficha['CTPS'] == 0:
        break
    else:
        ficha['Ano de contratacao'] = int(input('Ano de contratação: '))
        ficha['Salario'] = float(input('Salário: '))
        print()
        escolha = str(input('Digite [F] para finalizar: ')).strip().upper()[0]
        if escolha == 'F':
            break

print(f'Nome: {ficha["Nome"]}')
print(f'Idade: {anoatual - ficha["Ano de nascimento"]}')
print(f'CTPS: {ficha["CTPS"]}')
print(f'Ano de contratação: {ficha["Ano de contratacao"]}')
print(f'Salário: {ficha["Salario"]}')
print(f'Anos de serviço: {- anoatual - ficha["Ano de contratacao"]}')



