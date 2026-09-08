import random
maior = 0
menor = 0
num = 0

lista = random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)

for cont in range (len(lista)):
    num = (lista[cont])
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print(f'\033[1mOs numeros sorteados são:\033[m \033[1;32m{lista}\033[m')
print(f'\033[1mO maior numero é:\033[m \033[1;36m{maior}\033[m')
print(f'\033[1mO menor numero é:\033[m \033[1;35m{menor}\033[m')

