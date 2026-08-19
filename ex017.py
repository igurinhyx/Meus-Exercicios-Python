import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Agora o valor do cateto adjacente: '))
hipotenusa = (math.sqrt(co**2+ca**2))
print( 'A hipotenusa desse triangulo vale {:.2f}'.format(hipotenusa))