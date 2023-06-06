# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
produto1 = input('Qual produto deseja? ')
valor = float(input('Digite o valor do produto: '))

print('Produto encontrado!')
print('Produto: {}'.format(produto1))
print('Valor do produto: R${:.2f}'.format(valor))

nome = input('Qual seu nome? ')
print('PARÁBENS, {}! Você acaba de ganhar um desconto!'.format(nome))

desc = 5*valor/100
valor2 = valor - desc
print('Seu desconto será de 5% no valor do produto, {} no novo valor de R${:.2f}'.format(produto1, desc))
print('O produto agora está no valor de R${:.2f}'.format(valor2))