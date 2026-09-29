
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura:.2f}x{comprimento:.2f} é de {a:.2f}m².')


larg = float(input('LARGURA [M]: '))
comp = float(input('COMPRIMENTO [M]: '))
area(larg, comp)
