lista_num = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
num = 0
num_extenso = ''
while True:
    if 0 <= num <= 20:
        num = int(input('\033[1mDigite um numero\033[m \033[1;33mentre 0 e 20:\033[m '))
        if num <= 20:
            num_extenso = (lista_num[num])
    else:
        print('Você \033[1;31mnão digitou um número válido.\033[m \033[1;33mTente novamente!\033[m')
        num = int(input('\033[1mDigite um numero entre 0 e 20:\033[m '))
        if num <= 20:
            num_extenso = (lista_num[num])
    if 0 <= num <= 20:
        break
print(f'\033[1mVocê digitou:\033[m \033[1;32m{num_extenso}\033[m')


