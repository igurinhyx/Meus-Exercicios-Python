import time
lista = []

while True:
    valor = int(input('Digite um numero: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado!')
    else:
        print('O valor que você digitou, já está na lista! Por favor, digite outro')

    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    time.sleep(1)

    if escolha == 'N':
        break

lista.sort()

print(f'Sua lista, ficou assim: {lista}')
