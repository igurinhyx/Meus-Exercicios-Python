from random import randint
from time import sleep

lista = dict()
maior = menor = 0
for c in range(1, 5):
    jogador = randint(1, 6)
    print(f'O JOGADOR N°: {c}, tirou: {jogador}')
    sleep(1)
    lista[c] = jogador
print()
for c in lista:
    for l in lista:
        if c == 0:
            maior = menor = lista[c][l]
        else:
            if lista[c][l] > maior:
                maior = lista[c][l]
            if lista[c][l] < menor:
                menor = lista[c][l]
print(maior)
print(menor)