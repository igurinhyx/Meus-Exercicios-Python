print('Oie, vamos checar o seu KM okay?')
km_usuario = int(input('Qual o valor em KM que você atingiu? '))
km_multa = ((km_usuario - 80) * 7)
ultrapassou = km_usuario - 80
if km_usuario >= 81:
    print('Você foi multado em: {} por ultrapassar: {}'.format(km_multa, ultrapassou))
else:
    print('Parabéns! Você não tem nenhuma multa :D')