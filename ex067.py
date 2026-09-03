print('Quer ver a tabuada de qual valor?')
while True:
    num = int(input('\033[1mDigite aqui e se quiser PARAR [ - (n) ]:\033[m '))
    if num < 0:
        break
    print('_'*20)
    for c in range (1, 11):
        print(f'{num} x {c} = {num*c}')
    print('_' * 20)
print('FIM')