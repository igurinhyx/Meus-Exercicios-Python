import time

def titulo(msg):
    print('-'*(len(msg)+4))
    print(msg)
    print('-'*(len(msg)+4))

def jogador(comeco, vai, pulando):
    if pulando == 0:
        pulando = 1
    if comeco > vai:
        pulando = -abs(pulando)
        vai -= 1
    else:
        pulando = abs(pulando)
        vai += 1
    for c in range(comeco, vai, pulando):
        print(f'{c}', end=' ')
        time.sleep(0.5)
    print('FIM!')

titulo('  CONTADOR 1 - 10 - 1  ')
jogador(1, 10, 1)

titulo('  CONTADOR 10 - 0 - 2  ')
jogador(10, 0, -2)

titulo('  AGORA O SEU CONTADOR!  ')
comc = int(input('Começa do numero: '))
v = int(input('Vai até o numero: '))
pul = int(input('Pulando de: '))
jogador(comc, v, pul)