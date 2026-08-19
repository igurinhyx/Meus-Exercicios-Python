nome = str(input('Digite o nome de um lugar'))
dividir = nome.split()
primeiro_nome = dividir[0]
nome_santo = 'Santo' in primeiro_nome
print ('O nome tem SANTO?')
print ('Resposta: {}'.format(nome_santo))