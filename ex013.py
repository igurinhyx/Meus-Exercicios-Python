print('Que tal descobrir o quanto você passará a receber com o aumento de 15% ?')
nome = input('Digite seu nome:')
print('Olá! É um prazer{}.'.format(nome))
s = float(input('Agora, por favor, digite o valor do seu salário:'))
n1 = 15/100
n2 = s*n1
sf = s + n2
print('Certo! Pelo meus cálculos, como o valor antigo do seu salário era {} e passará a ser {}'.format(s,sf))
