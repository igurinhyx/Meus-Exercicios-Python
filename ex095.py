ficha = list()
jogador = dict()
gols = list()
while True:
    gols.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    jogador['Partidas'] = int(input(f'Quantidade de partidas do {jogador["Nome"]}: '))

    for c in range(0, jogador["Partidas"]):
        gol = int(input(f'Quantidade de gols na partida {c+1}: '))
        gols.append(gol)

    while True:
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print('Errado! Escreva S ou N')
        else:
            break
    jogador['Total'] = sum(gols)
    jogador['Gols'] = gols[:]
    ficha.append(jogador.copy())
    if escolha == 'N':
        break
print()
print('=='*40)
print('Cod  ', end= '')
for i in jogador.keys():
    print(f'{i:<15}', end= '')
print()
for k, v in enumerate(ficha):
    print(f'{k:>3}  ', end= '')
    for d in v.values():
        print(f'{str(d):<15}', end= '')
    print()
print('=='*40)
while True:
    resposta = int(input('Digite o numero do jogador que desejar OU [999 para parar]: '))
    if resposta == 999:
        break
    if resposta >= len(ficha):
        print('Erro! Esse jogador não existe.')
    else:
        print(f' | LEVANTAMENTO DO JOGADOR {ficha[resposta]["Nome"]} | ')
        for i, g in enumerate(ficha[resposta]['Gols']):
            print(f'No {i+1}° jogo, fez {g} gols.')
    print('=='*40)
print('<< ENCERRADO >>')


