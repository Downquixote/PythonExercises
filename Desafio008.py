# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
m1 = int(input('Digite a metragem: '))
cent = m1 * 100
mili = m1 * 1000

print('{} metros, {} centímetros, {} milímetros.'.format(m1, cent, mili))
