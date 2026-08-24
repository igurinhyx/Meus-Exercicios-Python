import time

print('\033[1;33m-=-\033[m'*20)
print('\033[1mCALCULO DE MÉDIA\033[m')
print('\033[1;33m-=-\033[m'*20)
time.sleep(2)

#Vou fazer umas gracinhas pro codigo ficar bonitinho
print('\033[1;36m_\033[m'*15)
nome_aluno = str(input('\033[1mDigite o nome completo do aluno:\033[m ')).strip().split()
print('Qual vai ser a média?')
print('1 --- MATÉRIAS EXATAS')
print('2 --- MATÉRIAS HUMANAS')
print('3 --- MATÉRIAS ESTRANGEIRAS')
print('4 --- MATÉRIAS ANUAIS')
print('5 --- TODAS AS MATÉRIAS')
escolha_materia = int(input('DIGITE O NÚMERO AQUI: '))
print('\033[1;36m_\033[m'*15)
time.sleep(2)

print('DIGITE AS NOTAS DE: ')
if escolha_materia == 1:
    biologia = float(input('\033[1mBIOLOGÍA: \033[m'))
    quimica = float(input('\033[1mQUÍMICA: \033[m'))
    fisica = float(input('\033[1mFÍSICA: \033[m'))
    media = (biologia+quimica+fisica)/3
elif escolha_materia == 2:
    historia = float(input('\033[1mHISTORIA: \033[m'))
    sociologia = float(input('\033[1mSOCIOLOGIA: \033[m'))
    geografia = float(input('\033[1mGEOGRAFIA: \033[m'))
    filosofia = float(input('\033[1mFILOSOFIA: \033[m'))
    media = (historia+sociologia+geografia+filosofia)/4
elif escolha_materia == 3:
    ingles = float(input('\033[1mINGLES: \033[m'))
    espanhol = float(input('\033[1mESPANHOL: \033[m'))
    frances = float(input('\033[1mFRANCES: \033[m'))
    media = (ingles+espanhol+frances)/3
elif escolha_materia == 4:
    portugues = float(input('\033[1mPORTUGUÊS: \033[m'))
    matematica = float(input('\033[1mMATEMATICA: \033[m'))
    artes = float(input('\033[1mARTES: \033[m'))
    educacao_fisica = float(input('\033[1mEDUCAÇÃO FISICA: \033[m'))
    media = (portugues+matematica+artes+educacao_fisica)/4
else:
    biologia = float(input('\033[1mBIOLOGÍA: \033[m'))
    quimica = float(input('\033[1mQUÍMICA: \033[m'))
    fisica = float(input('\033[1mFÍSICA: \033[m'))
    historia = float(input('\033[1mHISTORIA: \033[m'))
    sociologia = float(input('\033[1mSOCIOLOGIA: \033[m'))
    geografia = float(input('\033[1mGEOGRAFIA: \033[m'))
    filosofia = float(input('\033[1mFILOSOFIA: \033[m'))
    ingles = float(input('\033[1mINGLES: \033[m'))
    espanhol = float(input('\033[1mESPANHOL: \033[m'))
    frances = float(input('\033[1mFRANCES: \033[m'))
    portugues = float(input('\033[1mPORTUGUÊS: \033[m'))
    matematica = float(input('\033[1mMATEMATICA: \033[m'))
    artes = float(input('\033[1mARTES: \033[m'))
    educacao_fisica = float(input('\033[1mEDUCAÇÃO FISICA: \033[m'))
    media = (biologia+quimica+fisica+historia+sociologia+geografia+filosofia+ingles+espanhol+frances+portugues+artes+matematica+educacao_fisica)/14

time.sleep(1)
print('\033[1;33m-=-\033[m'*20)
print('\033[1mPROCESSANDO OS DADOS...\033[m')
print('\033[1;33m-=-\033[m'*20)
time.sleep(6)

#APROVADO OU REPROVADO
if media < 5.0:
    print('Situação ({}): \033[1;31mREPROVADO(A)\033[m'.format(nome_aluno[0]))
    print('MÉDIA DO ALUNO(a): \033[1;31m{:.2f}\033[m'.format(media))
    print('MÉDIA NECESSÁRIA: \033[1;31m5.0\033[m')
elif 5.0 > media <= 7.0:
    print('Situação ({}): \033[1;33mRECUPERAÇÃO\033[m'.format(nome_aluno[0]))
    print('MÉDIA DO ALUNO(a): \033[1;33m{:.2f}\033[m'.format(media))
    print('MÉDIA NECESSÁRIA: \033[1;33m7.0\033[m')
else:
    print('Situação ({}): \033[1;32mAPROVADO\033[m'.format(nome_aluno[0]))
    print('MÉDIA DO ALUNO(a): \033[1;32m{:.2f}\033[m'.format(media))
    print('MÉDIA NECESSÁRIA: \033[1;32m7.0\033[m')
