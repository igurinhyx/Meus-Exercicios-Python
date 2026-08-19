n1 = float(input('Digite o valor de algo:'))
print('O valor em metros é: {:.0f} \nO valor em decímetros é: {:.0f} \nO valor em centímetro é: {:.0f} \nE o valor em milímetros é: {:.0f}'.format(n1, n1*10, n1*10**2, n1*10**3))
print('Mas se você precisar do valor em Kilometros, Hectometros e Decametros, aqui está:')
print('O valor de {}M em Kilometros é: {}KM \nO valor em Hectometros é: {}HM \nO valor em Decametros é: {}DM'.format(n1, n1/10**3, n1/10**2, n1/10))
