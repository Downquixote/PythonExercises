nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))
print()

# Tipos primitivos,
# int = números inteiros
# float = pontos flutuantes
# boolean ou bool = verdadeiro ou falso
# str = string - escrita

n1 = int (input('Digite um número: '))
n2 = int (input('Digite mais um número: '))
s = n1 + n2
print('A soma entre {} e {} vale {} '.format(n1, n2, s))

# Para saber o tipo primitivo, use "type"... exemplo:

print(type(n1))
