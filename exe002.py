#Funçao que diz se valor na Var são letras. 
#Thursday, November7 2019
'''
n = input('Digite algo: ')
print(n.isalpha())
'''

# Crie um Programa que leia dois numeros e mostre a soma entre eles.
valid_n1 = False
while valid_n1 == False:
    n1 = input('Digite o número 1: ')
    try:
        n1 = float(n1)
        if n1 < 0:
            print('Digite um número maior que 0, por favor.\n')
        else:
            valid_n1 =True
    except:
        print('Digite somente números, não letras! E por gentileza, use somente ponto e não vírgula.\n')

valid_n2 = False
while valid_n2 == False:
    n2 = input('Digite o número 2: ')
    try:
        n2 = float(n2)
        if n2 < 0:
            print('Digite um número maior que 0, por favor.\n')
        else:
            valid_n2 =True
    except:
        print('Digite somente números, não letras! E por gentileza, use somente ponto e não vírgula.\n')


s = n1 + n2
print (f'A soma entre, {n1} e {n2} é: {s}')
