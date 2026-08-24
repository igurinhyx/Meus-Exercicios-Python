import time
import random
print('\033[1;36m-=-\033[m'*20)
print('\033[1mJOKENPÔ\033[m')
print('\033[1;36m-=-\033[m'*20)
time.sleep(2)

print('\033[1mOi! Eu sou o \033[1;33mBIMO\033[m e vou jogar jokenpo com você!\033[m \033[1;33m:D\033[m')
time.sleep(3)
print('\033[1mPrimeiro, após eu dizer "START!" eu vou escolher uma das seguintes opções: \033[m')
time.sleep(2)
print('\033[1;31mPEDRA\033[m, \033[1;35mPAPEL\033[m ou \033[1;33mTESOURA\033[m ')
time.sleep(2)
print('\033[1mMas, você já pode escolher o seu também! Mas só quando eu dizer "START" hein...')
time.sleep(2)
print('\033[1mBom, e agora que você já entendeu as regras, vamos começar...\033[m')
time.sleep(3)
print('\033[1;32mSTART!!!\033[m')
time.sleep(1)
print('"\033[1;31mPEDRA"\033[m, DIGITE 1')
print('"\033[1;33mTESOURA"\033[m, DIGITE 2')
print('"\033[1;35mPAPEL"\033[m, DIGITE 3')
escolha_jogador = int(input('\033[1;32mDIGITE AQUI:\033[m '))
time.sleep(2)
print('\033[1;36m-=-\033[m'*20)
print('\033[1mESTOU PENSANDO...\033[m')
print('\033[1;36m-=-\033[m'*20)
time.sleep(10)
print('\033[1;32mPENSEI!\033[1m')
time.sleep(2)
lista = [1, 2, 3]
escolha_computador = random.choice(lista)

print('\033[1mRESULTADO: \033[m')
if escolha_computador == escolha_jogador:
    print('\033[1;33mAHHHHH!! A gente empatou haha!\033[m')
    if escolha_computador == 3:
        print('Eu escolhi \033[1;35mPapel...\033[m')
    elif escolha_computador == 2:
        print('Eu escolhi \033[1;33mTesoura...\033[m')
    else:
        print('Eu escolhi \033[1;31mPedra...\033[m')

elif escolha_jogador == 2 and escolha_computador == 1 or escolha_jogador == 3 and escolha_computador == 2 or escolha_jogador == 1 and escolha_computador == 3:
    print('\033[1;31mMUAHAHAHAHAHHAHAHA!! EU GANHEI\033[m')
    if escolha_computador == 3:
        print('Eu escolhi \033[1;35mPapel BOBÃO\033[m')
    elif escolha_computador == 2:
        print('Eu escolhi \033[1;33mTesoura BOBÃO\033[m')
    else:
        print('Eu escolhi \033[1;31mPedra BOBÃO\033[m')
elif escolha_jogador == 3 and escolha_computador == 1 or escolha_jogador == 1 and escolha_computador == 2 or escolha_jogador == 2 and escolha_computador == 3:
    print('\033[1;32mAnão... você ganhou... :(\033[m')
    if escolha_computador == 3:
        print('Eu escolhi \033[1;35mPapel... maldito!\033[m')
    elif escolha_computador == 2:
        print('Eu escolhi \033[1;33mTesoura... maldito!\033[m')
    else:
        print('Eu escolhi \033[1;31mPedra...maldito!\033[m')


