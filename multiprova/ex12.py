# Escreva um programa que lê um número inteiro positivo N e em seguida cria uma lista com todos os números pares positivos menores do que N. O seu programa deve então percorrer essa lista e imprimir cada elemento dela com o comando print.

numerosP = []
N = int(input(''))
for x in range(0, N, 2):
    numerosP.append(x)

for x in range(0, N, 2):
  if x != 0:
    print(x)