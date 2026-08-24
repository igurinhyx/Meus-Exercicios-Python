import time
print('\033[1;33m-=-\033[m'*20)
print('\033[1mCALCULO DE PRODUTOS\033[m')
print('\033[1;33m-=-\033[m'*20)
time.sleep(2)

nome_produto = str(input('\033[1mDigite o nome do produto: \033[m')).strip().split()
preco_produto = float(input('\033[1mDigite o valor do {}: \033[m'.format(nome_produto[0])))
print('\033[1;33m-=-\033[m'*20)
print('\033[1mPROCESSANDO...\033[m')
print('\033[1;33m-=-\033[m'*20)
time.sleep(4)

#Fazendo a matemática

print('\033[1mVALOR:\033[m \033[1;32m{:.2f}\033[m'.format(preco_produto))
print('\033[1;32mEscolha o metodo de pagamento: \033[m')
print('\033[1mA VISTA DINHEIRO OU CHEQUE = 1\033[m')
print('\033[1mA VISTA CARTÃO = 2\033[m')
print('\033[1mDIVIDIR EM 2X = 3\033[m')
print('\033[1mDIVIDIR EM 3X OU MAIS = 4\033[m')
escolha = int(input('\033[1mDIGITE AQUI: \033[m'))
dinhero_cheque = preco_produto - (preco_produto * 10/100)
cartao_vista = preco_produto - (preco_produto * 5/100)
duas_vezes = preco_produto / 2
tres_vezes = (preco_produto / 3) + (20/100 * preco_produto)
print('\033[1;33m-=-\033[m'*20)
print('\033[1mPROCESSANDO...\033[m')
print('\033[1;33m-=-\033[m'*20)
time.sleep(4)


if escolha == 1:
    print('\033[1mVALOR TOTAL: {:.2f}R$\033[m'.format(dinhero_cheque))
elif escolha == 2:
    print('\033[1mVALOR TOTAL: {:.2f}R$\033[m'.format(cartao_vista))
elif escolha == 3:
    print('\033[1mVALOR TOTAL: {:.2f}R$\033[m'.format(duas_vezes))
elif escolha == 4:
    quantidade_vezes = float(input('\033[1mEm quantas vezes você quer dividir? \033[m'))
    print('\033[1;33m-=-\033[m' * 20)
    print('\033[1mPROCESSANDO...\033[m')
    print('\033[1;33m-=-\033[m' * 20)
    time.sleep(2)
    print('\033[1mVALOR TOTAL: {:.2f}R$\033[m'.format((preco_produto / quantidade_vezes) + (20/100 * preco_produto)))









