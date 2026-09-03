import random

vitorias = 0
while True:
    jogador = str(input('Escolha Par ou Impar [P / I]: ')).strip().upper()[0]
    if jogador == 'P':
        jogador = 'Par'
        computador = 'Impar'

    else:
        jogador = 'Impar'
        computador = 'Par'
    print(f'Certo! Eu escolho {computador}')
    print(f'{jogador}, {computador}')

    num_computador = random.randint(0, 10)
    num_jogador = int(input('Escolhe seu numero: '))
    soma = num_computador + num_jogador

    if jogador == 'Par' and soma % 2 == 0:
        print('Você venceu! Boa!')
        print(f'Eu escolhi {num_computador}, você escolheu {num_jogador} e a soma deu {soma}')
        vitorias +=1
    elif jogador == 'Impar' and soma % 2 != 0:
        print('Você venceu! Nice!')
        print(f'Eu escolhi {num_computador}, você escolheu {num_jogador} e a soma deu {soma}')
        vitorias += 1
    else:
        break
print(f'Bom, você perdeu e teve um total de {vitorias} vitorias')

