from random import randint
import time
computador = randint(0, 10)
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
    if num_jogador == computador:
        print('\033[1;32mCONGRAGULATIONSSS!!\033[m')
    else:
        print('\033[1;31mPEEESSIMOOOO!!\033[m Tenta de novo!!!'.format(computador))
    
