# Leia do teclado uma sequência de valores inteiros. Escreva uma função que recebe como parâmetro esta sequência de valores e imprime na tela quais elementos a compõem e quantas vezes estes aparecem nesta sequência.
# Exemplos:
# Entrada
# "1 2 3 4 5 6 7 8 8 7 6 5 1"
# Saída
# 1 = 2, 2 = 1, 3 = 1, 4 = 1 ,5 = 2 ,6 = 2 ,7 = 2 ,8 = 2
# Entrada
# "2 2 1 2 2 1"
# Saída
# 2 = 4, 1 = 2

num = input().split()

def valores(numeros):
    c = 0
    numer = []
    for x in range(len(numeros)):
        cx = numeros.count(numeros[x])
        numer.append(numeros[x])

        print(f'{numeros[x]} = {cx}')
        if numeros[x] not in numer:

            return cx

resultado = valores(num)