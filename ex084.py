pessoas = list()
nome = list()
qtd = 0
menor = 0
maior = 0
while True:
    nome.append(str(input('Nome: ')))
    nome.append(float(input('Peso: ')))
    pessoas.append(nome[:])
    nome.clear()
    qtd += 1

    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'A quantidade de pessoas cadastradas foram: {qtd}')


