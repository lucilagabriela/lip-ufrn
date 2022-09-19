# Escreva um programa que lê três números inteiros, onde cada número será fornecido em uma linha separada. O seu programa deve criar uma lista com esses números e em seguida remover dessa lista o maior e o menor elemento.

numeros = []

for x in range(3):
    nmr = int(input(''))
    numeros.append(nmr)

numeros.remove(max(numeros))
numeros.remove(min(numeros))
for c in range(1):
    print(numeros[c])