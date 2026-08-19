print('Que tal calcularmos o quanto você tem que gastar de tinta?')
b = float(input('Primeiro digite o valor da base da parede em metros:'))
h = float(input('Agora o valor da altura:'))
a = b*h
t = a/2
print('Certo, com o calculo feito, o valor de A (Área) da parede é exatamente: {}Metros'.format(a))
print('Agora entendendo que, o valor de 1 Litro de tinta cobre exatamente 2M(quadrados)\no valor da quantidade que você pode gastar de tinta por metro quadrado é exatamente igual a {}'.format(t))


