lista = list()
num = list()
pares = list()
soma = 0
soma_par = 0
for c in range(0, 9):
        valor = num.append(int(input(f'Digite o valor para [{c},{c}]: ')))
        lista.append(num[:])
        if num[0] % 2 == 0:
            pares.append(num[:])
        if c == 3:
            soma += valor
        if c == 6:
            soma += valor
        if c == 9:
            soma += valor

        num.clear()

print(lista[0:3])
print(lista[3:6])
print(lista[6:])
print(soma)

print()
for c in pares:
    soma_par = pares [c:c] + pares [c:c]
    c += 1
print(pares)
print(max(pares))
print(soma_par)








#for n in lista[:][:]:
    #if n % 2 == 0:
        #print(n)

#for n in lista[:][:]:
    #if n % 2 != 0:
        #print(n)