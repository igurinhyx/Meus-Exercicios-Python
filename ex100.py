from random import randint
from time import sleep

def sorteio(lista):
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end= ' ')
        sleep(0.5)

def somapar(lista):
    soma = 0
    pares = list()
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
            pares.append(valor)
    print(f'A soma dos pares vale: {soma}')
    print(f'Os números pares são: ', end= ' ')
    for valor in pares:
        print(f'{valor}', end= ' ')
        sleep(0.5)

numeros = list()
print('Os numeros sorteados são:', end= ' ')
sorteio(numeros)
sleep(1)
print()
somapar(numeros)
sleep(1)
