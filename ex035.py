print('Vamos ver se seu triângulo é realmente um triângulo!')
lado1 = float(input('Digite o valor do lado 1: '))
lado2 = float(input('Digite o valor do lado 2: '))
lado3 = float(input('Digite o valor do lado 3: '))
if lado1 < (lado2+lado3) and lado2 < (lado1+lado3) and lado3 < (lado2+lado1):
    print('Seu triângulo é um triângulo!')
else:
    print('ISSO NÃO É UM TRIÂNGULO!')

