# Operacoes Aritimeticas em python 3x 

''' 
+ adição
- subtração
* multiplicação
/ divisão
** potência
// divisão inteira
% resto da divisão
'''
# Ordem de Precedência
# 1 - {}
# 2 - **
# 3 - *, /, //, %
# 4 -  +, -

n1 = int(input('Uma valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}' .format(s, m, d), end=' ')
print('divisão inteira {} e potência {}' .format(di, e))