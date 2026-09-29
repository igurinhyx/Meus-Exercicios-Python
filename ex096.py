
def area(b, h):
    a = b * h
    print(f'A área de um terreno {b:.2f}x{h:.2f} é de {a}m².')



b = float(input('LARGURA [M]: '))
h = float(input('COMPRIMENTO [M]: '))
area(b, h)
