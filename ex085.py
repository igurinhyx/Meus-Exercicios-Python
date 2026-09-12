lista = list()

for c in range (0, 7):
    lista.append(int(input('Digite um numero: ')))

lista.sort()

print('Os numeros pares: ', end= ' ')
for c in lista:
    if c % 2 == 0:
        print(c, end= ' ')
print()
print('Os numeros impares: ', end= ' ')
for c in lista:
    if c % 2 != 0:
        print(c, end= ' ')
print()

print(f'A lista é: {lista}')
