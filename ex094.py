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

print()
print('=='*20)
print(f'[A] A media das idades é: {(soma/cont):.2f}')
print('=='*20)
print()

print('=='*20)
print(f'[B] A lista:')
for p in galera:
    for k, v in p.items():
        print(f'{k} | {v}')
    print('_'*10)
    print()
print('=='*20)
print()
print('=='*20)
print(f'[C] Quantidade de pessoas: {cont}')
print('=='*20)
print()

print('=='*20)
print(f'Lista de mulheres:')
for p in mulheres:
    for k, v in p.items():
        print(f'{k} | {v}')
    print('_'*10)
    print()
print('=='*20)
print()
print('=='*20)
print('[D] Quem tem idade acima da media: ')
for p in galera:
    if p["Idade"] >= (soma/cont):
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}')
        print()
print('=='*20)
print('ENCERRADO')