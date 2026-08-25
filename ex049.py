numero = int(input('Digite o número da tabuada escolhida: '))
multiplicacao = 0
for multiplicacao in range (0, 11 * numero):
        multiplicacao = multiplicacao * numero
        print ('A tabuada do {} é {}'.format(numero, multiplicacao))

