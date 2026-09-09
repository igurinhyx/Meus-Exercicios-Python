lista = ('Augusto', 'Pedro', 'Lucas', 'Gabriel',
'Ana', 'Felippe', 'Marcus', 'Luisa')

for nome in lista:
    print(f'\nNo nome: \033[1;31m{nome.upper()}\033[m, temos as vogais: ',end= ' ')
    for letra in nome:
        if letra.lower() in 'aeiou':
            print(f'\033[1;33m{letra.lower()}\033[m', end= ' ')