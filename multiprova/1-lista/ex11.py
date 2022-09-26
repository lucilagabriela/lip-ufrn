# Escreva um programa que lê um número inteiro positivo N e em seguida cria uma lista L1 com todos os números no intervalo de 1 até N. Depois, o seu programa deve criar uma cópia L2 da lista L1 e ler mais dois valores inteiros, V1 e V2, da entrada. O seu programa deve apagar da lista L1 os valores V1 e V2. Ao final, imprima as listas L1 e L2 com o comando print.

N = int(input(''))
L1 = []

for x in range(1, N+1): # N+1 para incluir o N
    L1.append(x)
L2 = L1[:] # cópia da lista L1

V1 = int(input(''))
V2 = int(input(''))

L1.remove(V1)
L1.remove(V2)

print(L1)
print(L2)