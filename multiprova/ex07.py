# Escreva um programa que lê um número inteiro positivo N e em seguida cria uma lista L com todos os números ímpares no intervalo de 1 até N. Depois, o seu programa deve ler dois valores inteiros, V1 e V2, da entrada e imprimir a soma dos elemento entre os índices V1 e V2 de L. Por exemplo, no caso da lista [1, 3, 5, 7, 9], a soma dos elementos entre os índices 1 e 3 (a sublista [3, 5, 7]) é igual a 15.

N = int(input(''))
lista = []
for x in range(1, N, 2):
    lista.append(x)
    print(lista)

V1 = int(input(''))
V2 = int(input(''))

