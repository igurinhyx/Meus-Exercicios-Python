lista = []

maior = 0
menor = 0
pos_maior = 0
pos_menor = 0
for c in range(0, 5):
    lista.append(int(input('Digite um valor: ')))

for c, l in enumerate(lista):
    if max(lista) == l:
        maior = l
        pos_maior = lista.index(maior)
    if min(lista) == l:
        menor = l
        pos_menor = lista.index(menor)

    print(f'Na posição {c + 1}, temos {l}')

print(maior)
print(menor)
print(pos_maior)
print(pos_menor)

