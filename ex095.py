ficha = dict()
gols = list()

while True:
    jogador = str(input('Nome do jogador: '))
    total_pt = int(input(f'Quantidade de partidas do {jogador}: '))

    for c in range(0, total_pt):
        gol = int(input(f'Quantidade de gols na partida {c+1}: '))
        gols.append(gol)

    while True:
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print('Errado! Escreva S ou N')
        else:
            break
    gols.clear()
    if escolha == 'N':
        break


