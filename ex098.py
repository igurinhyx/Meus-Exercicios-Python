import time

def titulo(msg):
    print('\033[1;33m-\033[m'*(len(msg)+4))
    print(msg)
    print('\033[1;33m-\033[m'*(len(msg)+4))

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

titulo('  \033[1;31mCONTADOR 1 - 10 - 1\033[m  ')
jogador(1, 10, 1)

titulo('  \033[1;31mCONTADOR 10 - 0 - 2\033[m  ')
jogador(10, 0, -2)

titulo('  \033[1;31mAGORA O SEU CONTADOR!\033[m  ')
comc = int(input('Começa do numero: '))
v = int(input('Vai até o numero: '))
pul = int(input('Pulando de: '))
jogador(comc, v, pul)