primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contagem = 0
raz = primeiro
total = 0
mais = 10
while mais != 0:
    total += mais
    while contagem <= total:
        print('{} -> '.format(raz), end='')
        raz += razao
        contagem += 1
    print('PAUSA')
    mais = int(input('Quantos você quer mostrar a mais: '))
print('FINAL')