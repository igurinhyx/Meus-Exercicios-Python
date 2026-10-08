
def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno \033[1;33m{largura:.2f}x{comprimento:.2f}\033[m é de \033[1;35m{a:.2f}m²\033[m.')

print('\033[1-=-'*20)
print('CONTROLE DE TERRENOS')
print('-=-'*20)
print()
print('=='*20)
larg = float(input('\033[1;32mLARGURA\033[m \033[1;34m[M]\033[m: '))
comp = float(input('\033[1;32mCOMPRIMENTO\033[m \033[1;34m[M]\033[m: '))
area(larg, comp)
print('=='*20)
