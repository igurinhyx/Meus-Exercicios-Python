lista_num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
num_extenso = ''
while True:
    num = int(input('\033[1mDigite um numero\033[m \033[1;33mentre 0 e 20:\033[m '))
    if 0 <= num <= 20:
        num_extenso = lista_num[num]
        print(f'\033[1mVoce digitou\033[m \033[1;32m{num_extenso}\033[m')
    else:
        print('Você \033[1;31mnão digitou um número válido.\033[m \033[1;32mTente novamente!\033[m')
    if 0 <= num <= 20:
        escolha = str(input('\033[1mDigite\033[m \033[1;31mF para finalizar\033[m \033[1;36mou\033[m \033[1;32mS para continuar\033[m: ')).strip().upper()[0]
        if escolha == 'F':
            break


print('\033[1;32mFIM\033[m')

