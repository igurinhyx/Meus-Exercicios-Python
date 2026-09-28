ficha = list()
jogador = dict()
gols = list()
while True:
    gols.clear()
    jogador['Nome'] = str(input('\033[1;33mNome\033[m do jogador: '))
    jogador['Partidas'] = int(input(f'Quantidade de \033[1;33mpartidas do {jogador["Nome"]}:\033[m '))

    for c in range(0, jogador["Partidas"]):
        gol = int(input(f'\033[1mQuantidade de\033[m \033[1;33mgols na partida {c+1}\033[m: '))
        gols.append(gol)

    while True:
        escolha = str(input('\033[1mQuer continuar?\033[m [\033[1;32mS\033[m/\033[1;31mN\033[m]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print('\033[1;33mErrado!\033[m Escreva \033[1;32mS\033[m ou \033[1;31mN\033[m')
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
    print(f'\033[1;35m{i:<15}\033[m', end= '')
print()
for k, v in enumerate(ficha):
    print(f'\033[1;34m{k:>3}\033[m  ', end= '')
    for d in v.values():
        print(f'\033[1;34m{str(d):<15}\033[m', end= '')
    print()
print('=='*40)
while True:
    resposta = int(input('Digite o numero do jogador que desejar OU [999 para parar]: '))
    if resposta == 999:
        break
    if resposta >= len(ficha):
        print('\033[1;33mErro!\033[m \033[1;31mEsse jogador não existe.\033[m')
    else:
        print(f' \033[1;35m| LEVANTAMENTO DO JOGADOR {ficha[resposta]["Nome"]} |\033[m ')
        for i, g in enumerate(ficha[resposta]['Gols']):
            print(f'No \033[1;36m{i+1}°\033[m jogo, fez \033[1;33m{g} gols.\033[m')
    print('=='*40)
print('<< ENCERRADO >>')


