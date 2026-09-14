lista = []

for c in range(0, 5):
    valor = (int(input(f'\033[1mDigite o\033[m \033[1;33m{c+1}°\033[m \033[1mvalor: \033[m')))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                break
        pos += 1

print()
print('\033[1mSua lista é:\033[m ')
print(f'\033[1;32m{lista}\033[m')