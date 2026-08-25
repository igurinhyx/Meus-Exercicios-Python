frase = str(input('Digite uma frase ou palavra: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print('A frase {} é um palíndromo: {}'.format(frase, inverso))
else:
    print('A frase {} não é um palíndromo: {}'.format(frase, inverso))