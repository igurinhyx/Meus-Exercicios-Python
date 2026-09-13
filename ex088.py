from random import randint
cont = 0
lista = list()

quantidade = int(input('Digite a quantidade de jogos que você precisa: '))
while True:
    num = randint(1, 60)
    if num not in lista:
        lista.append(num)
        cont += 1
    if cont >= 6:
        break
print(lista)

