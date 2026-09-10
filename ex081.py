cont = 0
lista = []
while True:
    valor = int(input('Digite um numero: '))
    lista.append(valor)
    cont += 1
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if escolha == 'N':
        break
lista.sort(reverse=True)
if 5 in lista:
    print(f'O cinco foi encontrado {lista.count(5)} vezes')
else:
    print('Cinco não foi encontrado')
print(f'Lista em ordem decrescente: {lista}')
print(f'Quantidade de numeros digitado: {cont}')