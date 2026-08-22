print('\033[1;36m-=-\033[m'*20)
print('\033[1mTRIÂNGULOS\033[m'*20)
print('\033[1;36m-=-\033[m'*20)

lado1 = float(input('Digite o valor do lado 1: '))
lado2 = float(input('Digite o valor do lado 2: '))
lado3 = float(input('Digite o valor do lado 3: '))

triangulo = lado1 < (lado2+lado3) and lado2 < (lado1+lado3) and lado3 < (lado2+lado1)
if triangulo and lado1 == lado2 and lado2 == lado3:
    print('Seu triângulo é \033[1;33mEQUILÁTERO\033[m')
elif triangulo and lado1 == lado3 or lado2 == lado1 or lado3 == lado2:
    print('Seu triângulo é \033[1;33mISÓCELES\033[m')
elif triangulo and lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
    print('Seu triângulo é \033[1;33mESCALENO\033[m')
else:
    print('ISSO NÃO É UM TRIÂNGULO!')