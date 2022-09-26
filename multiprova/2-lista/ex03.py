# Analisando o número de nascimentos
# Leia do teclado um valor inteiro n e em seguida uma sequência de n valores inteiros que representa a quantidade de nascimentos observados em uma cidade nos últimos n dias. Escreva um programa que imprima na tela o primeiro dia (índice da lista), excluindo-se o dia 0, em que se observa uma quantidade de nascimentos que é maior do que a soma de todos os nascimentos que o antecedem.

n = int(input(''))
lista = []
maior = 0
diaMaior = 0
for x in range(n):
    nasc = int(input(''))
    lista.append(nasc)
    maior += lista[x]
    for indice, valor in enumerate(lista):
        if lista[indice] > maior:
            diaMaior = indice
    if (indice != 0):
        print(f'dia {indice}')
    else:
        print('não há')