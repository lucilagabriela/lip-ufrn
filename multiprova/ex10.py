# Escreva um programa que lê o nome de três pessoas, onde cada nome será fornecido em uma linha separada. O seu programa deve criar uma lista com esses três nomes e imprimir a lista resultante com o comando print.

nomes = []
for x in range(3):
    nome = input('')
    nomes.append(nome)
print(nomes)