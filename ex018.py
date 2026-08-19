import math
angulo_graus = float(input('Qual o valor do angulo em graus: '))
angulo_rad = math.radians(angulo_graus)
print('O valor do seno é {:.2f}'.format(math.sin(angulo_rad)))