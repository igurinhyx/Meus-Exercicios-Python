lista = []
maior = 0
menor = 0
for c in range(0, 5):
    valor = lista.append(int(input('Digite um valor: ')))
    if c == 1:
        maior = menor = valor
        if valor > maior:
            lista.insert(c,valor)
        if valor < menor:
            lista.insert(c, valor)


print(lista)