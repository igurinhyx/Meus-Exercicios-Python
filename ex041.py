import datetime
import time

print('\033[1;36m-=-\033[m'*20)
print('\033[1mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m')
print('\033[1;36m-=-\033[m'*20)
time.sleep(2)

nome_atleta = str(input('\033[1mDIGITE O NOME DO ATLETA: \033[m')).strip().split()
time.sleep(2)

print('\033[1mDIGITE A DATA DE NASCIMENTO DO {}\033[m'.format(nome_atleta[0]))
dia_nascimento = int(input('\033[1mDIA: \033[m'))
mes_nascimento = int(input('\033[1mMÊS: \033[m'))
ano_nascimento = int(input('\033[1mANO: \033[m'))
hoje = datetime.date.today().year
time.sleep(2)

print('\033[1;36m-=-\033[m'*20)
print('\033[1mPROCESSANDO...\033[m')
print('\033[1;36m-=-\033[m'*20)
time.sleep(5)

if (hoje - ano_nascimento) <= 9:
    print('O atleta {} é \033[1;36mMIRIM\033[m'.format(nome_atleta[0]))
elif (hoje - ano_nascimento) <= 14:
    print('O atleta {} é \033[1;36mINFANTIL\033[m'.format(nome_atleta[0]))
elif (hoje - ano_nascimento) <= 19:
    print('O atleta {} é \033[1;36mJUNIOR\033[m'.format(nome_atleta[0]))
elif (hoje - ano_nascimento) >= 20:
    print('O atleta {} é \033[1;36SÊNIOR\033[m'.format(nome_atleta[0]))
else:
    print('O atleta {} é \033[1;36mSÊNIOR\033[m'.format(nome_atleta[0]))







