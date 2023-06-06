# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
tinta = area / 2

print('Sua parede tem a dimensão de {}x{}, a área da parede é {}m²'.format(altura, largura, area))
print('Quantidade necessária de tinta é de {} litros'.format(tinta))