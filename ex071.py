print('\033[1;34m=\033[m'*20)
print('\033[1;33mBANCO CEV\033[m')
print('\033[1;34m=\033[m'*20)
print(' ')
print('\033[1mQual o valor que você quer sacar?\033[m')
valor = int(input('\033[1;32mDigite aqui:\033[m '))
total = valor
ced = 50
total_ced = 0

while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total que receberá é: \033[1;33m{total_ced}\033[m cédulas de \033[1;32m{ced}R$\033[m')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        total_ced = 0
        if total == 0:
            break

