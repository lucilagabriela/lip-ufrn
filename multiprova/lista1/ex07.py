# Escreva um programa que lê um número inteiro positivo N e em seguida cria uma lista L com todos os números ímpares no intervalo de 1 até N. Depois, o seu programa deve ler dois valores inteiros, V1 e V2, da entrada e imprimir a soma dos elemento entre os índices V1 e V2 de L. Por exemplo, no caso da lista [1, 3, 5, 7, 9], a soma dos elementos entre os índices 1 e 3 (a sublista [3, 5, 7]) é igual a 15.

n = int(input(''))
soma = 0
numeros = []
for x in range(1, n+1, 2): # N+1 pois é para incluir o valor N
    numeros.append(x)

v1 = int(input(''))
v2 = int(input(''))

for x in range(v1, v2+1):
    soma += numeros[x]
print(soma)