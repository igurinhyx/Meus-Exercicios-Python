import random


lista = random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)
print(f'\033[1mOs numeros sorteados são:\033[m ', end=' ')
for c in lista:
    print(f'\033[1;32m{c}\033[m', end=' ')
print(f'\n\033[1mO maior numero é:\033[m \033[1;36m{max(lista)}\033[m')
print(f'\033[1mO menor numero é:\033[m \033[1;35m{min(lista)}\033[m')

