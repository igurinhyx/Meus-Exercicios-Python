matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spares = maior = scolunas = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite o valor para [{l},{c}]: '))
print()
print('\033[1mA matriz completa:\033[m ')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end= ' ')
        if matriz[l][c] % 2 == 0:
            spares += matriz[l][c]
    print()
print()
print(f'A soma dos pares vale: {spares}')
print()
print(f'A soma da coluna 3 vale: {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print()
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')