# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n1 = int(input('Digite um número para saber seu antecessor e sucessor: '))
n2 = 1
s = n1 + n2
sub = n1 - n2
print('Resultado antecessor: {}'.format(sub))
print('Resultado sucessor: {}'.format(s))