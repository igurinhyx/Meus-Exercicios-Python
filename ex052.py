num = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;33m', end= ' ')
        total += 1
    else:
        print('\033[31m', end= ' ')
    print('{}'.format(c), end=' ')
if total == 2:
    print('\n\033[mO número \033[1;32m{} é primo\033[m, porquê ele tem apenas \033[1;33m{}\033[m divisores. '.format(num, total))
else:
    print('\n\033[mO número \033[1;31m{} não é primo\033[m, pois ele tem \033[1;33m{}\033[m divisores. '.format(num, total))