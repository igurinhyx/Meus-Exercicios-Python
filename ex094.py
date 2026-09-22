
lista = list()
ficha = dict()
contagem = 0
mulheres = list()
soma = 0
while True:
    ficha['nome'] = str(input('Nome: '))
    ficha['sexo'] = str(input('Sexo: ')).strip().upper()[0]
    if ficha['sexo'] == 'M':
        ficha['sexo'] = 'Masculino'
    else:
        ficha['sexo'] = 'Feminino'
    ficha['idade'] = int(input('Idade: '))
    contagem += 1
    soma += ficha['idade']
    if ficha['sexo'] == 'Feminino':
        mulheres.append(ficha.copy())
    lista.append(ficha.copy())
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while escolha != 'S' or 'F':
        print('Por favor, digite S ou N.')
        if escolha == 'N':
            break
        if escolha == 'S':
            break
    if escolha == 'F':
        break



print(lista)
print(contagem)
media = soma / contagem
print(media)
print(mulheres)