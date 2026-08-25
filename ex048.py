soma = 0
for numero in range(1,501,2):
    if numero % 3 == 0:
        print('\033[1;32mÉ multiplo de 3\033[m o número: \033[1;35m{}\033[m'.format(numero))
        soma = soma + numero
    else:
        print('\033[1;31mNÃO é multiplo de 3\033[m o número: \033[1;35m{}\033[m'.format(numero))
print('E a soma entre TODOS os valores \033[1;32mVERDES\033[m é {}'.format(soma))
