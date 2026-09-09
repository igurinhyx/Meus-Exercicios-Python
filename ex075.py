nove = 0
n1 = int(input('Digite o 1 numero: '))
n2 = int(input('Digite o 2 numero: '))
n3 = int(input('Digite o 3 numero: '))
n4 = int(input('Digite o 4 numero: '))
lista = n1, n2, n3, n4

for cont in range (len(lista)):
    cont += 1
    nove = lista.count(9)

print(lista)
print(nove)
