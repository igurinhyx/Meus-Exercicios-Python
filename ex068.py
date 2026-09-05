import random
jogador = ' '
vitorias = 0
while True:
    while jogador not in 'PI':
        jogador = str(input('\033[1mEscolha\033[m \033[1;35mPar\033[m ou \033[1;36mImpar\033[m \033[1m[\033[m\033[1;35mP\033[m \033[1m/\033[m \033[1;36mI\033[m\033[1m]\033[m: ')).strip().upper()[0]
    if jogador == 'P':
        jogador = 'Par'
        computador = 'Impar'

    else:
        jogador = 'Impar'
        computador = 'Par'
    print(f'\033[1;32mCerto!\033[m \033[1mEu escolho\033[m \033[1;34m{computador}\033[m')
    print(f'\033[1;35m{jogador}\033[m, \033[1;36m{computador}\033[m')

    num_computador = random.randint(0, 10)
    num_jogador = int(input('Escolhe seu numero: '))
    soma = num_computador + num_jogador

    if jogador == 'Par' and soma % 2 == 0:
        print('\033[1;32mVocê venceu!\033[m \033[1;32mBoa!\033[m')
        print(f'\033[1mEu escolhi\033[m \033[1;33m{num_computador}\033[m, \033[1mvocê escolheu\033[m \033[1;33m{num_jogador}\033[m \033[1me a soma deu\033[m \033[1;32m{soma}\033[m')
        vitorias +=1
    elif jogador == 'Impar' and soma % 2 != 0:
        print('\033[1;32mVocê venceu!\033[m Nice!')
        print(f'\033[1mEu escolhi\033[m \033[1;33m{num_computador}\033[m, \033[1mvocê escolheu\033[m \033[1;33m{num_jogador}\033[m \033[1me a soma deu\033[m \033[1;32m{soma}\033[m')
        vitorias += 1
    else:
        break
print(f'\033[1mEu escolhi\033[m \033[1;33m{num_computador}\033[m, \033[1mvocê\033[m \033[1;33m{num_jogador}\033[m \033[1me a soma deu\033[m \033[1;31m{soma}\033[m')
print(f'\033[1;31mVocê perdeu\033[m e teve um total de \033[1;32m{vitorias} vitorias\033[m')

