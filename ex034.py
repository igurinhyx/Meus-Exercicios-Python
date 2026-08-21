import time
print('-=-'*20)
print('CALCULO DE AUMENTOS')
print('-=-'*20)
salario = float(input('INFORME SEU SALÁRIO: '))
time.sleep(2)
print('Processando...')
time.sleep(2)
if salario > 1250.00:
    print('O seu aumento é de {}, resultando em {}'.format('10%', ((salario*10/100)+salario)))
else:
    print ('O seu aumento é de {}, resultando em {}'.format('15%', ((salario*15/100)+salario)))
