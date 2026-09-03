idade = 0
cont_masculino = 0
cont_feminino = 0
cont_idade = 0
cont_idade_mulheres = 0
while True:
    idade = int(input('Digite a idade: '))
    if idade > 18:
        cont_idade += 1
    sexo = str(input('Sexo [M / F]: ')).strip().upper()[0]
    if sexo == 'M':
        sexo = 'Masculino'
        cont_masculino += 1
    else:
        sexo = 'Feminino'
        cont_feminino += 1
    if cont_masculino > 1:
        sexo_certo_homens = 'Homens'
    else:
        sexo_certo_homens = 'Homem'

    if cont_feminino > 1:
        sexo_certo_mulheres = 'Mulheres'
    else:
        sexo_certo_mulheres = 'Mulher'
    if idade < 20 and sexo == 'Feminino':
        cont_idade_mulheres += 1

    escolha = str(input('Quer continuar? [S / N]: ')).strip().upper()[0]
    if   escolha == 'N':
        break

print(f'''Certo!
A quantidade de pessoas maior que 18 anos é: {cont_idade}
A quantidade de homens cadastrados é: {cont_masculino}
A quantidade de {sexo_certo_mulheres} cadastradas é com menos de 20 anos é: {cont_idade_mulheres} ''')