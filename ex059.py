valor1 = int(input('Digite o \033[1mPRIMEIRO\033[m valor: '))
valor2 = int(input('Digite o \033[1mSEGUNDO\033[m valor: '))
escolha = 0
while escolha != 5:
    print('''[1] SOMAR 
[2] MULTIPLICAR
[3] MAIOR
[4] OUTROS NUMEROS
[5] FINALIZAR''')
    escolha = int(input('Digite a sua opção: '))

    if escolha == 1:
        soma = valor1 + valor2
        print('A soma do {} + {} é: {}'.format(valor1, valor2, soma))
    elif escolha == 2:
        multiplica = valor1 * valor2
        print('A multiplicação do {} * {} é: {}'.format(valor1, valor2, multiplica))
    elif escolha == 3:
        if valor1 > valor2:
            print('O valor {} é maior que o valor {}'.format(valor1, valor2))
        elif valor1 == valor2:
            print('Os valores são iguais')
        else:
            print('O valor {} é maior que o valor {}'.format(valor2, valor1))
    elif escolha == 4:
        valor1 = int(input('Digite o novo \033[1mPRIMEIRO\033[m valor: '))
        valor2 = int(input('Digite o novo \033[1mSEGUNDO\033[m valor: '))
    elif escolha == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
