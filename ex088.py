import random
contagem = 0
lista = list()
num = list()
escolha = int(input('Quantos jogos você vai querer? '))

while True:
    for c in range(0, escolha):
        for p in range(0, 6):
            num.append(random.randint(0, 60))
            while num not in lista:
                    lista.append(num[:])
            num.clear()

    contagem += 1
    if contagem == escolha:
        break
print(lista)

