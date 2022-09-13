# Escreva um programa que lê um número inteiro positivo N e em seguida cria uma lista L1 com todos os númeres pares positivos menores do que N. Depois, o seu programa deve fazer uma cópia L2 da lista L1 e ler dois valores inteiros, I1 e I2, da entrada. Você deve remover de L2 o elemento nos índice I1, e em seguida o elemento no índice I2. Após isso, imprima na saída as listas L1 e L2.

N = int(input(''))
L1 = []
for x in range(0, N, 2):
    if x != 0:
        L1.append(x)
L2 = L1[:] # cópia da lista

i1 = int(input(''))
i2 = int(input(''))
L2.pop(i1)
L2.pop(i2)

print(L1)
print(L2)