expressao = str(input('Digite a expressão: '))
lista = []

for simbolo in expressao:
    if simbolo == '(':
        lista.append('(')
    elif simbolo == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua lista é valida')
else:
    print('Sua lista não é valida')

