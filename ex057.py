genero = ''
while genero != 'M' and genero != 'F':
    genero = str(input('''Qual seu sexo? [M / F]
    Digite aqui: ''')).upper().strip()
    if genero == 'M':
        genero = 'Masculino'
        print('Anotado: {}'.format(genero))
    elif genero == 'F':
        genero = 'Feminino'
        print('Anotado: {}'.format(genero))
    else:
        print('Errado, tente novamente! ')
print('FIM')

