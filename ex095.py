ficha = list()
jogador = dict()
gols = list()
cod = 0
while True:
    gols.clear()
    cod += 1
    jogador['Cod'] = cod
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
    jogador['Gols'] = gols[:]
    ficha.append(jogador.copy())
    if escolha == 'N':
        break

print(ficha)
