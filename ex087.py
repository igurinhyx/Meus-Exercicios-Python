matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spares = maior = scolunas = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))
print()

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end= ' ')
        if matriz[l][c] % 2 == 0:
            spares += matriz[l][c]

    print()
print(spares)
print(matriz[0][2]+matriz[1][2]+matriz[2][2])

for l, matriz[1][] in range(0, 3):
    if l > matriz[1][l]:
        maior = l
print(maior)