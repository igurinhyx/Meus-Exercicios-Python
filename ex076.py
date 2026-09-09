lista = (
    'Pão', 1.50,
    'Leite', 4.25,
    'Café', 5.25,
    'Queijo', 4.50,
    'Peixe', 10.50,
)
print('\033[1;34m-=-\033[m'*10)
print('LISTA DE PRODUTOS: ')
print('\033[1;34m-=-\033[m'*10)

for produto in range (0, len(lista)):
    if produto % 2 == 0:
        print(f'\033[1m{lista[produto]:<10}\033[m',end= '')
    if produto % 2 != 0:
        print(f'\033[1;33m{lista[produto]:>7.2f}\033[m \033[1;32mR$\033[m')

