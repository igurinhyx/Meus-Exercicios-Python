from datetime import date
import time

print('\033[1;33m-=-\033[m'*20)
print('ALISTAMENTO MILITAR')
print('\033[1;33m-=-\033[m'*20)
time.sleep(2)

ano_nascimento = int(input('\033[1mDigite o ano em que você nasceu: \033[m'))
dia_nascimento = int(input('\033[1mDigite o dia em que você nasceu: \033[m'))
mes_nascimento = int(input('\033[1mDigite o mês em que você nasceu: \033[m'))

print('\033[1;33m-=-\033[m'*20)
print('PROCESSANDO...')
print('\033[1;33m-=-\033[m'*20)
time.sleep(5)

hoje = date.today().year

if ( hoje - ano_nascimento ) > 18:
    print('Já passou do tempo de se alistar! Vá o quanto antes!!')
elif ( hoje - ano_nascimento ) == 18:
    print('Você está no tempo certo de alistamento. Aliste-se!')
else:
    print('Você não precisa se alistar ainda! ')
