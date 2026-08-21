import time
print('\033[1;33m-=-\033[m'*20)
print('\033[1mPROGRAMA DE EMPRÉSTIMO\033[m')
print('\033[1;33m-=-\033[m'*20)

nome = (str(input('Por gentileza, \033[1mdigite seu nome:\033[m'))).strip().split()

print('\033[1;33m-=-\033[m'*20)
print('\033[1mPROCESSANDO...\033[m')
print('\033[1;33m-=-\033[m'*20)
time.sleep(4)

print('Certo, {}! '.format(nome[0]))
print('\033[1mAgora responda essas perguntas:\033[m')
time.sleep(2)

print('\033[1;36m=\033[m'*20)
valor_casa = float(input('\033[1mQual o valor da casa que você pretende comprar?\033[m '))
print('\033[1;36m=\033[m'*20)
salario = float(input('\033[1mQual o valor do seu salário hoje?\033[m '))
print('\033[1;36m=\033[m'*20)
anos = float(input('\033[1mEm quantos anos você pretende pagar?\033[m '))
print('\033[1;36m=\033[m'*20)
time.sleep(3)

print('\033[1;33m-=-\033[m'*20)
print('\033[1mPROCESSANDO...\033[m')
print('\033[1;33m-=-\033[m'*20)
time.sleep(5)

prestacao = valor_casa / ( anos * 12 )

if prestacao > 30/100 * salario:
    print('{}, sentimos em lhe informar.'.format(nome[0]))
    print('O valor estabelecido na prestação \033[1;31multrapassa 30% do valor do seu salário.\033[m')
    time.sleep(2)
    print('\033[1mValor da prestação:\033[m {:.2f}'.format(prestacao))
    print('\033[1m30% do seu salário:\033[m {:.2f}'.format(30/100 * salario))
    time.sleep(3)
    print('Por isso, o \033[1;31mseu empréstimo estará sendo negado.\033[m ')
else:
    print('{}, tenho uma notícia ótima!'.format(nome[0]))
    print('O valor estabelecido na prestação, \033[1;32mnão ultrapassa 30% do valor do seu salário.\033[m')
    time.sleep(2)
    print('\033[1mValor da prestação:\033[m {:.2f}'.format(prestacao))
    print('\033[1m30% do seu salário:\033[m {:.2f}'.format(30 / 100 * salario))
    time.sleep(3)
    print('Por isso, \033[1;32mseu empréstimo estará sendo aceito!.\033[m ')
