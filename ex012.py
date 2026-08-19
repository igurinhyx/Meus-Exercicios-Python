print('OLHA A PROPRO! \nCUPOM COM 5% de DESCONTOOOO!! GARANTA JÁ!')
nome = input('Digite seu nome:')
p = input('Digite qual produto você quer garantir:')
v = float(input('Digite o valor do produto:'))
n1 = 5/100
n2 = n1*v
vf = v-n2
print('Parabéns! {}'.format(nome))
print('O valor do seu produto passou de {} para {:.2} com apenas uma PROPRO'.format(v,vf))


