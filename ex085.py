
lista_pares = list()
lista_impares = list()
lista = list()

for c in range (0, 7):
    lista.append(int(input('Digite um numero: ')))

for p, num in enumerate(lista):
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
lista.sort()
lista_impares.sort()
lista_pares.sort()
print(lista)
print(lista_pares)
print(lista_impares)
