resp = 'S'
media = soma = cont = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite o numero: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        if maior == menor:
            maior = menor
    resp = str(input('Quer continuar? [S / N]: ')).strip().upper()[0]

media = soma / cont
print('Você digitou {} numeros e a media é {:.2f}'.format(cont, media))
if maior != menor:
    print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
elif maior == menor:
    print('Os valores são iguais, portanto não tem maior e nem menor')

