idade = 0
cont_masculino = 0
cont_feminino = 0
cont_idade = 0
cont_idade_mulheres = 0

while True:
    sexo = ' '
    escolha = ' '
    print('\033[1;31m_\033[m'*30)
    idade = int(input('\033[1mDigite a\033[m \033[1;32midade:\033[m '))
    if idade > 18:
        cont_idade += 1
    print('\033[1;31m_\033[m'*30)
    while sexo not in 'MF':
        sexo = str(input('\033[1mSexo\033[m \033[1;32m[M / F]:\033[m ')).strip().upper()[0]
        if sexo not in 'MF':
            print('\033[1;31mDigitação não válida\033[m, \033[1;32mescolha [M / F]\033[m')
    if sexo == 'M':
        cont_masculino += 1
    else:
        cont_feminino += 1
    if cont_masculino > 1:
        sexo_certo_homens = 'Homens'
    else:
        sexo_certo_homens = 'Homem'

    if cont_feminino > 1:
        sexo_certo_mulheres = 'Mulheres'
    else:
        sexo_certo_mulheres = 'Mulher'
    if idade < 20 and sexo == 'F':
        cont_idade_mulheres += 1
    print('\033[1;31m_\033[m'*30)
    while escolha not in 'SN':
        escolha = str(input('\033[1;33mQuer continuar?\033[m \033[1m[\033[m\033[1;32mS\033[m \033[1m/\033[m \033[1;31mN\033[m\033[1m]\033[m: ')).strip().upper()[0]
    if   escolha == 'N':
        break

print(f'''Certo!
A quantidade de pessoas maior que 18 anos é: {cont_idade}
A quantidade de homens cadastrados é: {cont_masculino}
A quantidade de {sexo_certo_mulheres} cadastradas é com menos de 20 anos é: {cont_idade_mulheres} ''')