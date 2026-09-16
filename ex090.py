
ficha = list()
situacao = ''
aluno = dict()

aluno['nome'] = str(input('\033[1;35mNome\033[m do \033[1;36maluno(a):\033[m '))
aluno['media'] = float(input(f'\033[1;35mMedia\033[m do(a) \033[1;36m{aluno["nome"]}\033[m: '))

if aluno['media'] < 7:
    situacao = 'Reprovado(a)'
else:
    situacao = 'Aprovado(a)'

print(f'Nome: \033[1;34m{aluno["nome"]}\033[m')
if aluno['media'] < 7:
    print(f'Media: \033[1;31m{aluno["media"]}\033[m')
else:
    print(f'Media: \033[1;32m{aluno["media"]}\033[m')
if situacao == 'Aprovado(a)':
    print(f'Esse aluno(a) está: \033[1;32m{situacao}\033[m')
else:
    print(f'Esse aluno(a) está: \033[1;31m{situacao}\033[m')


