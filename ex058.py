from random import randint
import time
computador = randint(0, 10)
tentativas = 0
num_jogador = 0
print('-=-'*20)
print('\033[1;33mVou pensar em um número entre 0 e 10, tente adivinhar!\033[m')
print('-=-'*20)
time.sleep(3)
print('\033[1;31m-=-\033[m'*20)
print('\033[1;33mPENSANDO...\033[m')
print('\033[1;31m-=-\033[m'*20)
time.sleep(7)
print('Qual numero eu pensei?')
while num_jogador != computador:
    num_jogador = int(input('Digite aqui: '))
    time.sleep(2)
    tentativas += 1
    if num_jogador == computador:
        print('\033[1;32mCONGRAGULATIONSSS!!\033[m Você só precisou de {} tentaivas! '.format(tentativas))
    else:
        print('\033[1;31mPEEESSIMOOOO!!\033[m Tenta de novo!!!'.format(computador))
        if tentativas > 3:
            print('\033[1;31mErrou de novo\033[m, era de se esperar né? Vou te dar outra chance...')
        elif tentativas > 5:
            print('\033[1;31mSeu talento para adivinhar\033[m as coisas é de berço, só \033[1;31mfaltou nascer!\033[m')
        elif tentativas > 7:
            print('\033[1;31mMermão, MELHORE!!\033[m')
        elif tentativas > 9:
            print('\033[1;31mDEPOIS DE TER CHUTADO TODOS OS NÚMEROS É FACIL!!!\033[m')