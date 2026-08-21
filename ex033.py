n1 = float(input('Digite um número qualquer: '))
n2 = float(input('Agora outro: '))
n3 = float(input('E outro: '))

if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

if n1>n2 and n1>n3:
    maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O maior numero é {} e o menor {}'.format(maior, menor))