from random import randint
from time import sleep

def sorteio(lista):
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'\033[1;32m{n}\033[m', end= ' ')
        sleep(0.5)

def somapar(lista):
    soma = 0
    pares = list()
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
            pares.append(valor)
    print(f'\033[35mA soma dos pares vale:\033[m \033[1;32m{soma}\033[m')
    sleep(1)
    print(f'\033[35mOs números pares são:\033[m ', end= ' ')
    for valor in pares:
        print(f'\033[1;32m{valor}\033[m', end= ' ')
        sleep(0.5)

numeros = list()
print('\033[35mOs numeros sorteados são:\033[m', end= ' ')
sorteio(numeros)
print()
somapar(numeros)
