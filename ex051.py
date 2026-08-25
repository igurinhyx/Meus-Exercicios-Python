termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao ):
    print('{}'.format(c), end = ' \033[1;31m-> \033[m')
print('FINAL')