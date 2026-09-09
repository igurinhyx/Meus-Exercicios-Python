num = (int(input('Digite \033[1;32mum numero: \033[m')),
int(input('Digite \033[1;32moutro numero: \033[m')),
int(input('Digite \033[1;32mmais um numero: \033[m')),
int(input('Digite \033[1;32mo ultimo numero: \033[m')))
print(f'\033[1mA sua lista é:\033[m \033[1;35m{num}\033[m')
print(f'\033[1mO numero\033[m \033[1;34m9 foi encontrado\033[m \033[1;36m{num.count(9)} vezes\033[m')
if 3 in num:
    print(f'O número \033[1;34m3 foi encontrado\033[m na \033[1;35m{num.index(3) + 1}° posição\033[m')
else:
    print('O \033[1;31mvalor 3 não foi encontrado\033[m em nenhuma posição')
print('Os \033[1;33mvalores pares\033[m são: ', end= ' ')
for n in num:
    if n % 2 == 0:
        print(f'\033[1;33m{n}\033[m', end= ' ')

