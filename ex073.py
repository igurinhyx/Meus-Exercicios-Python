times = 'Athletico-PR','Atlético-MG', 'Bahia', 'Botafogo', 'Chapecoense', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Flamengo', 'Fluminense', 'Grêmio', 'Internacional', 'Mirassol', 'Palmeiras', 'Red Bull', 'Bragantino', 'RemoSantos', 'São Paulo', 'Vasco', 'Vitória'
colocados = 'Flamengo', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Bahia'
colocados_4 = 'Vasco da Gama', 'Internacional', 'Clube do Remo', 'Chapecoense'
ordem = sorted(times)
ultimo = 'Chapecoense'

while True:
    print('\033[1;32m=\033[m' * 35)
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
    if escolha == 'a':
        for cont in range (len(times)):
            print(f'\033[1;35m{cont + 1}\033[m \033[1;36m{times[cont]}\033[m')
    elif escolha == 'b':
        for cont in range (len(colocados)):
            print(f'\033[1mEm\033[m \033[1;35m{cont+1}º lugar\033[m, \033[1;36m{colocados[cont]}\033[m')
    elif escolha == 'c':
        cont_1 = 16
        for cont in range (len(colocados_4)):
            cont_1 += 1
            print(f'\033[1mEm\033[m \033[1;35m{cont_1}º lugar\033[m, \033[1;36m{colocados_4[cont]}\033[m')
    elif escolha == 'd':
        for cont in range(len(ordem)):
            print(f'\033[1;36m{ordem[cont][0]}\033[m\033[1m{ordem[cont][1:]}\033[m')
    elif escolha == 'e':
        print(f'\033[1mO\033[m \033[1;31multimo colocado\033[m \033[1mfoi:\033[m \033[1;31m{ultimo}\033[m')
    elif escolha == 'f':
        break
print('FIM')
print('\033[1;32m=\033[m' * 25)


