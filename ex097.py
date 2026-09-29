def escreva(msg):
    print('\033[1;35m-\033[m'*(len(msg)+4))
    print(msg)
    print('\033[1;35m-\033[m'*(len(msg)+4))


escreva('  \033[1;34mIGOR\033[m  ')
print()
escreva('  \033[1;34mCURSO DE PROGRAMAÇÃO\033[m  ')
