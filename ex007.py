nome = input('Qual o nome do aluno?')
turma = input('Qual a turma do aluno?')
n1 = int(input('Me diga as notas de História'))
n2 = int(input('Me diga as notas de Sociologia'))
n3 = int(input('Me diga as notas de Filosofia'))
n4 = int(input('Me diga as notas de Geografia'))
print('O aluno {}, da turma {}, tem a media de {}'.format(nome, turma, (n1+n2+n3+n4)/4))


