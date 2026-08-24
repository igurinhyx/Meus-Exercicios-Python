print('\033[1;33m=-=\033[m'*20)
print('\033[1mCONVERSÃO DE BASES\033[m')
print('\033[1;33m=-=\033[m'*20)
numero = int(input('Digite o numero INTEIRO que você quer converter: '))
print('''Escolha um dos seguintes itens: 
[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL ''')
escolha = int(input('DIGITE AQUI: '))

if escolha == 1:
    print('O numero {} em BINARIO é {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O numero {} em OCTAL é {}'.format(numero, oct(numero)[2:]))
else:
    print('O numero {} em HEXADECIMAL é {}'.format(numero, hex(numero)[2:]))
