print ('Vamos fazer o calculo final do seu pagamento')
d = int(input('Quantos dias você alugou o carro?'))
km = float(input('Quantos KM você percorreu?'))
print ('O valor total a pagar é exatamente {:.2f}'.format((d * 60) + (km * 0.15)))
