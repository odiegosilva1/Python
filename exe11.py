# Comparando números

n1 = float(input("Digíte um número: "))
n2 = float(input("Digíte outro número: "))

if n1 < n2:
  print("O numero", n1, "é maior que", n2)
elif n1 > n2:
  print("O número", n2, "é menor que", n1)
else:
  print("Os números são iguais")