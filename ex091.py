from random import randint
from time import sleep

jogo = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)
}
print()
for k, v in jogo.items():
    print(f'O \033[1;35m{k}\033[m tirou: \033[1;34m[\033[m\033[1;36m{v}\033[m\033[1;34m]\033[m')
    sleep(1)