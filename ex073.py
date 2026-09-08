times = 'Athletico-PR','Atlético-MG', 'Bahia', 'Botafogo', 'Chapecoense', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Grêmio', 'Internacional', 'Mirassol', 'Palmeiras', 'Red Bull', 'Bragantino', 'RemoSantos', 'São Paulo', 'Vasco', 'Vitória'
colocados = 'Flamengo', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Bahia'
colocados_4 = 'Vasco da Gama', 'Internacional', 'Clube do Remo', 'Chapecoense'
ordem = sorted(times)
ultimo = 'Chapecoense'

while True:
    print('Escolha uma das opções à seguir: ')
    print('''
\033[1;34m[a]\033[m \033[1mOs 20 times do Brasileirão\033[m
\033[1;34m[b]\033[m \033[1mOs 5 primeiros colocados\033[m
\033[1;34m[c]\033[m \033[1mOs 4 ultimos colocados\033[m
\033[1;34m[d]\033[m \033[1mOs times em ordem alfabética\033[m
\033[1;34m[e]\033[m \033[1mO ultimo colocado\033[m
\033[1;31m[f]\033[m \033[1;31mFinalizar\033[m''')
    print(' ')
    print('\033[1;32m=\033[m' * 35)
    escolha = str(input('\033[1;34mDigite aqui: \033[m')).strip().lower()[0]
    print('\033[1;32m=\033[m' * 35)
    if escolha == 'a':
        for cont in range (len(times)):
            print((cont + 1), times[cont])
    elif escolha == 'b':
        for cont in range (len(colocados)):
            print(f'Em {cont+1}º lugar, {colocados[cont]}')
    elif escolha == 'c':
        cont_1 = 16
        for cont in range (len(colocados_4)):
            cont_1 += 1
            print(f'Em {cont_1}º lugar, {colocados_4[cont]}')
    elif escolha == 'd':
        for cont in range(len(ordem)):
            print(f'{ordem[cont]}')
    elif escolha == 'e':
        print(f'O ultimo colocado foi: {ultimo}')
    elif escolha == 'f':
        break
print('FIM')
print('\033[1;32m=\033[m' * 25)


