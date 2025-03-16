# Soma Resto


n1 = int(input("Digite nota 1: "))
n2 = int(input("Digite nota 2: "))
n3 = int(input("Digite nota 3: "))
n4 = int(input("Digite nota 4: "))

soma = n1 + n2 + n3 + n4 
resto = soma%2

print("A soma dos números é ",soma)
print("O resto da soma dos números é ",resto)


if resto == 1:
  print("A soma é Impar")
else:
  print("A soma é par")  