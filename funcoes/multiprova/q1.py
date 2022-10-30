# Considere as definições de média, moda e mediana dadas a seguir para um conjunto v de n valores inteiros ordenados:
# Média: somatório de todos os elementos do conjunto dividido pela quantidade de elementos;
# Moda: valor que mais vezes ocorre no conjunto;
# Mediana: é igual ao elemento central do conjunto, caso este possua uma quantidade ímpar de elementos. Caso a quantidade de elementos seja par, então a mediana é a média dos dois elementos centrais;
# A partir da definição dada, implemente uma função que recebe como argumento um vetor de números inteiros  e retorna sua média, moda e mediana. Implemente também um programa para testar essa função a partir de valores fornecidos pelo usuário. Exemplo:
# Entrada
# 5
# 1 2 3 3 5
# Saída
# (media, moda, mediana) = (2.80, 3, 3.00)

def valores(vetor):
    listaC = []
    soma = 0
    c = 0
    moda = vetor[0]
    #mediana, media, moda = 0
    #central, central1, central2 = 0

    for x in range(len(vetor)):
        soma += vetor[x]
        media = soma/len(vetor)

    for x in range(len(vetor)):
        cx = vetor.count(vetor[x])
        c1 = vetor.count(moda)
        if cx > c1:
            moda = vetor[x]

    if len(vetor) % 2 == 0:
        central1 = (len(vetor)//2)-1
        central2 = (len(vetor)//2)
        mediana = (vetor[central1]+vetor[central2])/2
    else:
        central = (len(vetor)+1)//2
        mediana = vetor[central]

    return (media, moda, mediana)

lista = []
n = int(input())
for x in range(n):
    numero = int(input())
    lista.append(numero)
lista.sort()

resultado = valores(lista)
print(f'(media, moda, mediana) = ({resultado[0]:.2f}, {resultado[1]}, {resultado[2]:.2f})')