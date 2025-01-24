numero = int(input("Digite um número:"))
fatorial = numero
while numero >= 2:
  fatorial = fatorial * (numero - 1)
  numero -= 1
print(fatorial)