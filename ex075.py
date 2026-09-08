nove = 0
n1 = int(input('Digite o 1 numero: '))
n2 = int(input('Digite o 2 numero: '))
n3 = int(input('Digite o 3 numero: '))
n4 = int(input('Digite o 4 numero: '))
lista = n1, n2, n3, n4

for cont in range (0, 5):
    n1 = int(input(f'Digite o {cont} numero: '))
    cont += 1
    nove = lista.count(9)

print(lista[0])
print(nove)
print(lista.index(3))