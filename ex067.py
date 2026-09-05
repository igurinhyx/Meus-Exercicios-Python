print('\033[1;32mQuer ver a tabuada de qual valor?\033[m')
while True:
    num = int(input('\033[1mDigite aqui e se quiser\033[m \033[1;31mPARAR [ - (n) ]\033[m: '))
    if num < 0:
        break
    print('\033[1;36m_\033[m'*20)
    for c in range (1, 11):
        print(f'\033[1;33m{num}\033[m \033[1;31mx\033[m \033[1;33m{c}\033[m = \033[1;32m{num*c}\033[m')
    print('\033[1;36m_\033[m'* 20)
print('FIM')