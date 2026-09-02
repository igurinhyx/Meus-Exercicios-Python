primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contagem = 0
raz = primeiro
while contagem <= 10:
    print('{} -> '.format(raz), end='')
    raz += razao
    contagem += 1
print('FINAL')