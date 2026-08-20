km_rodado = float(input('Digite os kilometros rodados: '))
acima_200 = km_rodado * 0.45
abaixo_200 = km_rodado * 0.50
if acima_200:
    print('Por percorrer {}, você terá que pagar {:.2f}'.format(km_rodado,acima_200))
else:
    print('Por percorrer {}, você terá que pagar {:.2f}'.format(km_rodado,abaixo_200))