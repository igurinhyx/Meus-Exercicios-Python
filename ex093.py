dicionario = dict
ficha = dict()
partidas = dict()
partidas_lista = []
soma = 0
ficha['jogador'] = str(input('Nome (jogador): '))
ficha['partidas'] = int(input('Partidas jogadas: '))
for c in range(ficha['partidas']):
    partidas['gols'] = int(input(f'Digite o valor de gols da {c+1}° partida: '))
    partidas_lista.append(partidas['gols'])
    soma += partidas['gols']
dicionario.copy(ficha)


print(soma)
print(dicionario)