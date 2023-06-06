# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com aumento de 15%.
nomefun = input('Digite o nome do funcionário: ')
print('Olá, {}!'.format(nomefun))
cargo = input('Qual seu cargo? ')
salario = float(input('Digite o valor do seu salário: '))

print('Há uma alteração em sua remuneração!')
aumen = salario * 15 / 100

print('Seu salário teve um acréscimo de 15%, equivalente há R${:.2f}'.format(aumen))
newsala = aumen + salario
print('Salário atual: R${:.2f}'.format(newsala))