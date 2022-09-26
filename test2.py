n = int(input(''))
lista = []
maior = 0
diaMaior = 0
i = 0
for x in range(n):
    nasc = int(input(''))
    lista.append(nasc)
    maior += lista[x]
    #i += 1
    if lista[x] < maior:
        diaMaior = x
    else:
        print(f'dia {i}')