def maior(* num):
    print('=='*30)
    print()
    print('Temos os números:', end=' ')
    for valor in num:
        print(f'{valor}', end= ' ')
        if valor == 0:
            max = valor

    print()
    print(f'No total, temos: {len(num)} números passados')
    print(f'O maior valor é: {max(num)}')


maior(2, 0, 3, 6, 3, 5)
maior(4, 7, 2, 6)
maior(2, 5, 6)
maior(6, 8)
maior()

