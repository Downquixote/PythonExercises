# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))

alu = 60 * dias
kmroda = 0.15 * km
valor = alu + kmroda

print('Valor dos dias alugados: R${:.2f}'.format(alu))
print('Valor dos KM rodados: R${:.2f}'.format(kmroda))
print('Valor cobrado: R${:.2f}'.format(valor))