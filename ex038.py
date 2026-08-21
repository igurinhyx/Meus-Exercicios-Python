import time

#VARIAVEIS:

a = int(input('\033[1mDigite um numero inteiro:\033[m '))
time.sleep(2)
b = int(input('\033[1mDigite outro numero inteiro:\033[m '))
time.sleep(2)

#PROCESSANDO:
print('\033[1;33m-=-\033[m'*20)
print('PROCESSANDO...')
print('\033[1;33m-=-\033[m'*20)

if a > b:
    print('O primeiro valor é maior')
elif b > a:
    print('O segundo valor é maior')
else:
    print('Ambos valores são iguais.')
