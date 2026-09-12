lista = list()
num = list()
for c in range(0, 9):
        num.append(int(input(f'Digite o valor para [{c},{c}]: ')))
        lista.append(num[:])
        num.clear()
print(lista)

print(lista[0:3])
print(lista[3:6])
print(lista[6:])