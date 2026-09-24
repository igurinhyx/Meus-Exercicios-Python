ficha
jogador = dict()
gols = list()

while True:
    ficha['Nome'] = str(input('Nome do jogador: '))
    ficha['Partidas'] = int(input(f'Quantidade de partidas do {ficha["Nome"]}: '))

    for c in range(0, ficha["Partidas"]):
        gol = int(input(f'Quantidade de gols na partida {c+1}: '))
        gols.append(gol)

    while True:
        escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print('Errado! Escreva S ou N')
        else:
            break
    ficha['Gols'] = gols[:]
    gols.clear()
    if escolha == 'N':
        break

print(ficha)
