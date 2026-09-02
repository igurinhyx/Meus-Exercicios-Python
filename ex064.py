num = 0
soma = 0
cont = 0
print('Digite um numero ou [999] para PARAR')
while num != 999:
    num = int(input('\033[1mDigite aqui:\033[m '))
    soma += num
    cont += 1
print('A soma entre os valores é: {}'.format(soma - 999))
print('A quantidade de números digitados foi: {}'.format(cont - 1))