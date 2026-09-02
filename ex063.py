print('SEQUENCIA FIBONACCI')
n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
contador = 3
print('{} - {} - '.format(t1, t2), end='')
while contador <= n:
    t3 = t1 + t2
    print('{} - '.format(t3),end='')
    t1 = t2
    t2 = t3
    contador += 1
print('FINAL')