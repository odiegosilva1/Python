count = 0

while count < 3:
  name = str(input("Digite um nome: "))
  print("você digitou o nome", name)
  # Atualiza para não cair em loop inf
  count += 1