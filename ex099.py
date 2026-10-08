import time

def maior(* num):
    cont = max = 0
    print('=='*30)
    print('Temos os números:', end=' ')
    for valor in num:
        print(f'{valor}', end= ' ')
        time.sleep(0.5)
        if cont == 0:
            max = valor
        else:
            if valor > max:
                max = valor
        cont += 1
    print()
    print(f'No total, temos: {len(num)} números passados')
    print(f'O maior valor é: {max}')
    time.sleep(0.5)
    print('Processando...')
    time.sleep(0.5)

print('=-='*20)
print(f'{'ANALISE DE DADOS':>35}')
print('=-='*20)

maior(2, 0, 3, 6, 3, 5)
maior(4, 7, 2, 6)
maior(2, 5, 6)
maior(6, 8)
maior()
print('==' * 30)
print()
print('=-='*20)
print(f'{'FIM!':>35}')
print('=-='*20)


