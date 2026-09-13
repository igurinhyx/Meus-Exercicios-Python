from random import randint
from time import sleep
lista = list()
jogos = list()
total = 1

print('=-='*20)
print('MEGA SENA')
print('=-='*20)
quantidade = int(input('Digite a quantidade de jogos que você precisa: '))
while total <= quantidade:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

for l, c in enumerate(jogos):
    print(f'Jogo {l+1}: {c}')
    sleep(1)



