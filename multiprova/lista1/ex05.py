# Escreva um programa que lê quatro números inteiros, onde cada número será fornecido em uma linha separada. O seu programa deve criar uma lista com esses números e em seguida remover dessa lista os dois menores elementos. Ao final, imprima cada elemento da lista conforme abaixo.

numeros = []
for x in range(4):
    numero = int(input(''))
    numeros.append(numero)

for x in range(2):
  numeros.remove(min(numeros))

for x in range(2):
    print(numeros[x])