jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome (jogador): '))
total = int(input(f'Quantidades de partidas que o {jogador['Nome']}, jogou: '))

for c in range(0, total):
    partidas.append(int(input(f'Quantos gols o {jogador['Nome']} fez na {c+1}° partida: ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print()
print(jogador)
print()
for k, v in jogador.items():
    print(f'{k}: {v}')
print()
print(f'O {jogador["Nome"]} jogou: {len(partidas)} partidas')
print()
for i, v in enumerate(jogador['Gols']):
    print(f'Na {i + 1}° partida, o {jogador["Nome"]} marcou {v} gols.')
