###import random
###n0 = str('0')
###n1 = str('1')
###n2 = str('2')
###n3 = str('3')
###n4 = str('4')
###n5 = str('5')
###n_a = (n0,n1,n2,n3,n4,n5)
###sorte = random.choice(n_a)
###print('Pensei em um número inteiro entre 0 e 5... Será que você consegue adivinhar qual é?')
###print('Qual o número que eu pensei')
###numero_usuario = str(input('Digite aqui: '))
###if numero_usuario == sorte:
    ###print('Parabéns!! Você é bom mesmo hein...')
###else:
    ###print('Você é péssimo nisso! Eu ganhei... hahaha')
###print('AMOOOOOOOOOO')###


from random import randint

computador = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número, tente adivinhar...')
print('-=-'*20)
num = int(input('Qual numero eu pensei: '))
if num == computador:
    print('PARABENS!')
else:
    print('Pessimo! Eu pensei no {}!!!'.format(computador))