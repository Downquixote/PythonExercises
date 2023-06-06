# Desafios
print('Para somar dois números inteiros, veja a seguir:')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2

print('A soma entre {} e {}, o resultado é {}'.format(n1, n2, s))
print(type(n1))

print()

n = input('Digite algo: ')
print('Só tem números? ', n.isnumeric())
print('É alfábetico? ', n.isalnum())
print('É decimal? ', n.isdecimal())
print('É maiúsculo? ', n.isupper())
print('Há letras? ', n.isalpha())
