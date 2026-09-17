from operator import itemgetter
from random import randint
from time import sleep
cont = 1
jogo = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6)
}
ranking = list()
print()
for k, v in jogo.items():
    print(f'O \033[1;35m{k}\033[m tirou: \033[1;34m[\033[m\033[1;36m{v}\033[m\033[1;34m]\033[m')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'O {i+1}° lugar vai para o: {v[0]} com {v[1]}')
