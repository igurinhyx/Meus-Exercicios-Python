
lista = list()
medias = list()
nome = list()
while True:
    nome.append(str(input('Nome: ')))
    media1 = medias.append(float(input('Media 1: ')))
    media2 = medias.append(float(input('Media 2: ')))
    lista.append(nome[:])
    lista.append(medias[:])
    nome.clear()
    medias.clear()
    escolha = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if escolha == 'N':
        break
print(lista)