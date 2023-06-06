# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. US$ 1,00 = R$ 4,92
real = float(input('Saldo disponível em carteira: R$'))
dolar = real / 4.92

print('Com R${}, você pode comprar US${:.2f}'.format(real, dolar))
