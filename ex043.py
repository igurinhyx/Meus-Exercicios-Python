import time
print ('\033[1;33m-=-\033[m'*20)
print ('\033[1m                    CALCULADORA DE IMC\033[m')
print ('\033[1;33m-=-\033[m'*20)

#Guardando a variável de nome do usuario + o novo, já que fiz um split
nome_usuario = str(input('Por gentileza, \033[1mdigite seu nome completo: \033[m')).strip().split()
nome_usuario_novo = nome_usuario[0]
print ('\033[1;33m-=-\033[m'*20)
print ('                    \033[1mEstou processando...\033[m')
print ('\033[1;33m-=-\033[m'*20)
time.sleep(2)
print ('Certo! \033[1;32mÉ um prazer {}!\033[m Me chamo BIMO e eu vou calcular seu IMC.'.format(nome_usuario_novo))
time.sleep(4)
print ('Mas para eu calcular seu IMC vou precisar das seguintes informações: ')
time.sleep(4)
#Guardando as variaveis para peso e altura, com float caso o valor seja quebrado
peso_kg = float(input('\033[1;36mPESO EM KG (KILOGRAMAS):\033[m '))
altura_m = float(input('\033[1;36mALTURA EM M (METROS):\033[m '))

#Aqui ele reafirma as informações pro usuário checar rapidamente se está tudo ok
print ('ESSAS SÃO AS INFORMAÇÕES QUE VOCÊ ENVIOU:')
print ('\033[1;34m_\033[m'*10)
print ('\033[1;36mNOME:\033[m \033[1m{}\033[m '.format(nome_usuario_novo))
print ('\033[1;36mPESO:\033[m \033[1m{:.2f}\033[m '.format(peso_kg))
print ('\033[1;36mALTURA:\033[m \033[1m{:.2f}\033[m '.format(altura_m))
print ('\033[1;34m_\033[m'*10)
time.sleep(5)
print ('Agora que já tenho tudo que preciso, irei analisar seu IMC.')
time.sleep(3)
print ('Até logo! :D')
time.sleep(3)
print ('\033[1;33m-=-\033[m'*20)
print('         \033[1mEU SOU BIMO E ESTOU PROCESSANDO...\033[m')
print ('\033[1;33m-=-\033[m'*20)
time.sleep(10)

#CALCULO do IMC
imc = peso_kg / (altura_m ** 2)

#Condições pra retorno
if imc < 18.5:
    print('Eita...')
    time.sleep(2)
    print('Eu analisei seu IMC {}, mas não foi muito bom...'.format(nome_usuario_novo))
    time.sleep(3)
    print('Infelizmente tenho que te confirmar, mas com \033[1;31m{:.2f}\033[m de IMC \033[1;31mvocê está abaixo do peso!\033[m :( '.format(imc))
    time.sleep(5)
    print('Porém, não fique triste! Há diversas maneiras de melhorar isso.')
    time.sleep(3)
elif 18.5 <= imc < 25:
    print('Olha só!')
    time.sleep(2)
    print('Analisando seu IMC, \033[1;32mvocê está no peso adequado\033[m, com um IMC de \033[1;32m{:.2f}\033[m'.format(imc))
    time.sleep(4)
    print('Meus parabéns, {}!!'.format(nome_usuario_novo))
    time.sleep(3)
elif 25 <= imc <30 :
    print('Hmm...')
    time.sleep(3)
    print('Seu IMC não está legal!')
    time.sleep(3)
    print('Está em \033[1;31m{:.2f}\033[m, significa que \033[1;31mvocê está acima do peso!\033[m'.format(imc))
    time.sleep(5)
    print('Mas fica tranquilo, {}! Dá para reverter essa situação <3'.format(nome_usuario_novo))
    time.sleep(3)
elif 30 <= imc < 40:
    print('Hmm...')
    time.sleep(3)
    print('Seu IMC não está legal!')
    time.sleep(3)
    print('Está em \033[1;31m{:.2f}\033[m, significa que \033[1;31mVocê está obeso!\033[m'.format(imc))
    time.sleep(5)
    print('Mas fica tranquilo, {}! Dá para reverter essa situação <3'.format(nome_usuario_novo))
    time.sleep(3)
else:
    print('Hmm...')
    time.sleep(3)
    print('Seu IMC não está legal!')
    time.sleep(3)
    print('Está em \033[1;31m{:.2f}\033[m, significa que \033[1;31mvocê com obesidade mórbida!\033[m'.format(imc))
    time.sleep(5)
    print('Mas fica tranquilo, {}! Dá para reverter essa situação <3'.format(nome_usuario_novo))
    time.sleep(3)
#FIM
time.sleep(3)
print ('\033[1;33m-=-\033[m'*20)
print ('  \033[1mESPERO TER AJUDADO! ASS: BIMO :D\033[m')
print ('\033[1;33m-=-\033[m'*20)