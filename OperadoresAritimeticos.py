n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# \n para quebrar a linha, para não quebrar use end=''

print('A soma é {} \n A subtração é {} \n A multiplacação é {} \n A divisão é {:.3f}'.format(s, sub, m, d), end=' ')
print(' A Divisão Inteira é {} \n A Potência é {}'.format(di, e))