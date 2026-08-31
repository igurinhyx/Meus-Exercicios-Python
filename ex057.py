sexo = str(input('[M / F] informe seu sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, digite novamente: ')).strip().upper()[0]
if sexo == 'F':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'
print('Sexo listado com sucesso: {}'.format(sexo))
