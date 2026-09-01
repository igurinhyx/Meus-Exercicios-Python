qtd_homens = 0
mediaidade = 0
maioridade_homem = 0
nome_homem_maior = ''
totmulher20 = 0
qtd_mulheres = 0
sexo_certo_homens = 'Indefinido'
sexo_certo_mulheres = 'Indefinido'
somaidade = 0
for p in range (1, 5):
    print('\033[1;31m-=-\033[m'*10, '\033[1m{}ª PESSOA\033[m'.format(p), '\033[1;31m-=-\033[m'*10)
    nome = str(input('NOME: ')).strip().title()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO[M/F]: ')).upper().strip()
    somaidade += idade

#Mulheres com menos de 20 anos:
    if sexo == 'F' and idade <= 20:
        totmulher20 += 1

#Qual homem é mais velho:
    if p == 1 and sexo == 'M':
        maioridade_homem = idade
        nome_homem_maior = nome
    else:
        if idade > maioridade_homem and sexo == 'M':
            maioridade_homem = idade
            nome_homem_maior = nome

#Quantos homens e quantas mulheres tem:
    if sexo == 'M':
        sexo_certo_homens = 'Homem'
        qtd_homens += 1
        if qtd_homens > 1:
            sexo_certo_homens = 'Homens'
    if sexo == 'F':
        sexo_certo_mulheres = 'Mulher'
        qtd_mulheres += 1
        if qtd_mulheres > 1:
            sexo_certo_mulheres = 'Mulheres'

mediaidade = somaidade / 4
print('Temos {} {}'.format(qtd_homens, sexo_certo_homens))
print('Temos {} {}'.format(qtd_mulheres, sexo_certo_mulheres))
print('A média da idade entre as 4 pessoas é: {:.2f}'.format(mediaidade))
print('O homem mais velho é: {} com {} anos'.format(nome_homem_maior, maioridade_homem))
print('A quantidade de mulheres com menos de 20 anos é: {}'.format(totmulher20))