print('Quer ver a tabuada de qual valor?')
while True:
    num = int(input('\033[1mDigite aqui e se quiser PARAR [ - (n) ]:\033[m '))
    if num < 0:
        break
    print('_'*20)
    print(f'''
{num} x 1 = {num*1}
{num} x 2 = {num*2}
{num} x 3 = {num*3}
{num} x 4 = {num*4}
{num} x 5 = {num*5}
{num} x 6 = {num*6}
{num} x 7 = {num*7}
{num} x 8 = {num*8}
{num} x 9 = {num*9}
{num} x 10 = {num*10}''')
    print('_' * 20)
print('FIM')