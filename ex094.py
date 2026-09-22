galera = list()
pessoa = dict()
mulheres = list()
cont = 0
soma = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))

    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        else:
            print('Errado, digite apenas M ou F')

    if pessoa['Sexo'] == 'F':
        pessoa['Sexo'] = 'Feminino'
    else:
        pessoa['Sexo'] = 'Masculino'

    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    cont += 1
    if pessoa['Sexo'] == 'Feminino':
        mulheres.append(pessoa.copy())
    while True:
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print('Errado, digite S ou N')
        else:
            break
    if escolha == 'N':
        break


print(f'A media das idades é: {soma/cont}')
print(pessoa)
print(galera)
print(cont)
print(f'Mulheres{mulheres}')