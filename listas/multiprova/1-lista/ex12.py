# Escreva um programa que lê um número inteiro positivo N e em seguida cria uma lista com todos os números pares positivos menores do que N. O seu programa deve então percorrer essa lista e imprimir cada elemento dela com o comando print.

n = int(input(''))
numeros = []
for x in range(0, n, 2):
    if x != 0:
        numeros.append(x)
for x in range(len(numeros)):
    print(numeros[x])