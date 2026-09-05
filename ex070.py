soma = 0
qtd_prod = 0
menor = 0
nome_menor = ''
cont = 0
while True:
    escolha = ' '
    nome_produto = str(input('Digite o nome do produto: ')).strip().title()[0:]

    preco = float(input('Digite o preço do produto: '))
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
        escolha = str(input('Quer continuar? [S / N]: ')).strip().upper()[0]
        if escolha not in 'SN':
            print('Digitação invalida, digite [S / N]')
    if escolha == 'N':
        break
print(f'''\033[1mO total gasto na compra foi:\033[m \033[1;32m{soma}R$\033[m
A quantidade de produtos que custam mais de 1,000R$ é: \033[1;32m{qtd_prod}\033[m
O nome do produto mais barato é: \033[1;32m{nome_menor}\033[m que custa {menor}R$\033[m''')