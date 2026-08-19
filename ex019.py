import random
n1 = str(input('Nome 1: '))
n2 = str(input('Nome 2: '))
n3 = str(input('Nome 3: '))
n4 = str(input('Nome 4: '))
n5 = str(input('Nome 5: '))
lista = (n1,n2,n3,n4,n5)
sort = random.choice(lista)
print('O sorteado é: {}'.format(sort))

