from random import randint
from time import sleep

def sorteio(lista):
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end= ' ')
        sleep(0.5)


numeros = list()
print('Sorteando...')
sorteio(numeros)
print('[ Pronto! ]', end= '')

