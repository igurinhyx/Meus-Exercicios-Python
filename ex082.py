lista = []
lista_pares = []
lista_impares = []

while True:
    valor = int(input('Digite um numero: '))
    lista.append(valor)
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break

print(f'Lista completa: {lista}')
print(f'Lista completa dos PARES: {lista_pares}')
print(f'Lista completa dos IMPARES: {lista_impares}')