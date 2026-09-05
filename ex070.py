soma = 0
qtd_prod = 0
menor = 0
nome_menor = ''
cont = 0

print('\033[1;34m=\033[m' * 40)
print('\033[1;36m{:^40}\033[m'.format('MERCADINHO DO ZÉ'))

while True:
    escolha = ' '
    print('\033[1;34m=\033[m'*40)
    nome_produto = str(input('\033[1mDigite\033[m \033[1;33mo nome do produto:\033[m ')).strip().title()[0:]
    print('\033[1;34m=\033[m'*40)
    preco = float(input('\033[1mDigite\033[m o \033[1;33mpreço do produto:\033[m '))
    soma += preco
    if preco > 1000:
        qtd_prod += 1
    if cont == 1:
        menor = preco
        nome_menor = nome_produto.strip().title()[0:]
    else:
        if preco < menor:
            menor = preco
            nome_menor = nome_produto.strip().title()[0:]
        if menor == menor:
            menor = preco
            nome_menor = nome_produto.strip().title()[0:]
    while escolha not in 'SN':
        print('\033[1;34m=\033[m' * 40)
        escolha = str(input('\033[1;33mQuer continuar?\033[m [\033[1;32mS\033[m / \033[1;31mN\033[m]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print('Digitação invalida, digite [S / N]')
    if escolha == 'N':
        break
print(f'''\033[1mO total gasto na compra foi:\033[m \033[1;32m{soma}R$\033[m
\033[1mA quantidade de produtos que \033[1;31mcustam mais de\033[m \033[1;32m1,000R$\033[m é:\033[m \033[1;32m{qtd_prod}\033[m
\033[1mO nome do produto mais barato é:\033[m \033[1;32m{nome_menor}\033[m \033[1mque custa\033[m \033[1;32m{menor}R$\033[m''')