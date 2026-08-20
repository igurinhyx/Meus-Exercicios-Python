num = int(input('Digite um número INTEIRO: '))
par = num % 2 == 0
if par:
    print('O número: {} é par!'.format(num))
else:
    print('O número: {} é impar.'.format(num))
