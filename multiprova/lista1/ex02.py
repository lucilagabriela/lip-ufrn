# Escreva um programa que lê o nome de 3 pessoas, onde cada nome será fornecido em uma linha separada. O seu programa deve criar uma lista com o comprimento desses nomes e imprimir a lista resultante com o comando print.
pessoas = []
tamanhos = []
for x in range(0, 3):
    pessoa = input((''))
    pessoas.append(pessoa)

for c in range(3):
    tamanhos.append(len(pessoas[c]))

print(tamanhos)