"""
Print recebe um argumento e imprime uma mensagem.
Usar sep='' separa os argumentos não nomeados


print(11, 12)
print(11, 12, sep='-')
print(11, 12, sep='', end='\n')

# Caracter de Escape
print('linha 1 \'linha 2')

#r 
print(r"Diego \"Silva\"")


# tipos de dados primitivos
# int : 0 ou -1
# float : 1;5 0u -1-5
# str : texto 'texto'


print( type('deigo) )
Funcão type mostra o tipo do dado
"""

nome = 'Diego'
sobrenome = 'Silva'
idade = 32
ano_nascimento = 2025 - idade
maior_de_idade = idade >= 18
altura_metros = 1.66


print('Nome:', nome)
print('Sobrenone', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento: ', ano_nascimento)
print('È mainor de Idade? ', maior_de_idade)
print('Altura em metros:', altura_metros)   







