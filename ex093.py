jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome (jogador): '))
total = int(input(f'Quantidades de partidas que o {jogador['Nome']}, jogou: '))

for c in range(0, total):
    partidas.append(int(input(f'Quantos gols o {jogador['Nome']} fez na {c+1}° partida: ')))
print(jogador)
print(partidas)