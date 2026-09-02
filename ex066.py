s = c = 0

while True:
    num = int(input('Digite um numero ou [999] - PARAR: '))
    if num == 999:
        break
    c += 1
    s += num
print(f'A soma dos números digitados é: {s}')
print(f'E você digitou exatamente: {c} numeros')