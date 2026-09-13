ficha = list()


while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    escolha = str(input('Quer continuar? [S/N]:  ')).strip().upper()[0]
    if escolha == 'N':
        break

print(f'\033[1m{"N°.":<4} {"Nome":<10} {"Media":>8}\033[m')
print('\033[1m==\033[m'*25)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}')
print('\033[1m==\033[m'*25)

while True:
    escolha2 = int(input('Quer ver as notas de qual aluno? [999 PARAR]: '))
    if escolha2 == 999:
        print('FINALIZANDO...')
        break
    if escolha2 <= len(ficha) - 1:
        print(f'Notas de {ficha[escolha2][0]}: {ficha[escolha2][1]}')


