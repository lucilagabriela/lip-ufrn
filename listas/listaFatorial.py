listaNumeros = input().split()
listaNumeros = [int(i) for i in listaNumeros]
listaFatoriais = []

for x in listaNumeros: #para cada elemento na lista
    fatorial = 1
    for i in range(1, x+1): #para cada elemento no intervalo [1, elem da lista]
        fatorial *= i
    listaFatoriais.append(fatorial)
print(listaFatoriais)