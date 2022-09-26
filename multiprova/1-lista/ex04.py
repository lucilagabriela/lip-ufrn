# Escreva um programa que lê quatro números inteiros, onde cada número será fornecido em uma linha separada. O seu programa deve criar uma lista com esses números e em seguida remover dessa lista os dois maiores elementos. Ao final, imprima a lista resultante com o comando print.

numeros = []
#primeiroMaior = 0
#segundoMaior = 0

for x in range(4):
  nmrs = int(input(''))
  numeros.append(nmrs)

for c in range(2):
	numeros.remove(max(numeros))

print(numeros)