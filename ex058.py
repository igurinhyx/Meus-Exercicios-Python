from random import randint
import time
num_computador = randint(0, 10)
num_jogador = 0
tentativas = 0
acertou = False
print('-=-'*20)
print('\033[1;33mVou pensar em um número entre 0 e 10, tente adivinhar!\033[m')
print('-=-'*20)
time.sleep(2)
print('\033[1;31m-=-\033[m'*20)
print('\033[1;33mPENSANDO...\033[m')
print('\033[1;31m-=-\033[m'*20)
time.sleep(4)
print('Qual numero eu pensei?')
while not acertou:
    num_jogador = int(input('Digite aqui: '))
    tentativas += 1
    if num_computador == num_jogador:
        acertou = True
        print('Boa! Acertou com {} tentativas'.format(tentativas))
    elif num_computador != num_jogador:
        if 0 <= tentativas <= 4:
            print('Tenta de novo!! ')
        elif 4 < tentativas <= 8:
            print('Caraca! Acerta isso logo')
        elif tentativas > 8:
            print('Agora que você acerta né...')
        if num_computador > num_jogador:
            print('Meu número é maior do que o seu...')
        if num_computador < num_jogador:
            print('Meu número é menor que o seu...')

