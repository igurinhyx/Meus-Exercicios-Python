lista = []

for cont in range(0, 5):
    lista.append(int(input(f'Digite um valor para a \033[1;32mposição {cont}:\033[m ')))

print(f'A sua lista deu: {lista}')
print(f'O \033[1;33mmaior valor é:\033[m \033[1;31m{max(lista)}\033[m ')
print('E ele \033[1mapareceu nas posições:\033[m ', end= ' ')
for pos, valor in enumerate(lista):
    if valor == max(lista):
        print(f'\033[1;32m{pos}\033[m...', end= ' ')

print()
print(f'O \033[1;34mmenor valor\033[m é: \033[1;36m{min(lista)}\033[m')
print('E ele \033[1mapareceu nas posições: \033[m', end= ' ')
for pos, valor in enumerate(lista):
    if valor == min(lista):
        print(f'\033[1;32m{pos}\033[m...', end= ' ')


