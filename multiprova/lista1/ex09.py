# Escreva um programa que lê o nome de quatro pessoas, onde cada nome será fornecido em uma linha separada. O seu programa deve criar uma lista ordenada com os nomes dessas pessoas e imprimir a lista resultante com o comando print.

nomes = []
for x in range(4):
    nome = input('')
    nomes.append(nome)
nomes.sort()
print(nomes)