num = [[], []]

for c in range (1, 8):
    valor = (int(input(f'Digite o {c}° numero: ')))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)

num[0].sort()
num[1].sort()
print(f'Os numeros pares: {num[0]} ', end= ' ')

print()
print(f'Os numeros impares: {num[1]}', end= ' ')
