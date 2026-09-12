temporario = []
principal = []
maior = menor = 0
while True:

    temporario.append(str(input('Digite o nome: ')))
    temporario.append(float(input('Digite o peso: ')))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha in 'N':
        break
print(f'Os dados foram: {principal}')
print(f'A quantidade de dados salvos foram: {len(principal)}')
print()
print(f'As pessoas com os maiores pesos foram: ', end= ' ')
for pessoa in principal:
    if pessoa[1] == maior:
        print(f'{pessoa[0]} com {maior} |', end=' ')
print()
print(f'As pessoas com os menores pesos foram: ', end= ' ')
for pessoa in principal:
    if pessoa[1] == menor:
        print(f'{pessoa[0]} com {menor} |', end=' ')
