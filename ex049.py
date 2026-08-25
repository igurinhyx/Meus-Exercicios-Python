print('Está com dificuldade na tabuada?')
n1 = int(input('Digita um número aí: '))
print('-'*12)
for c in range (0, 11):
        print('{} x {} = {}'.format(n1,c,n1*c))
print('-'*12)
