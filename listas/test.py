# q3 lista3
n = int(input(''))
nascimentos = []
for x in range(n):
    nascimentos.append(int(input()))

resposta = False
for dia in range(1, n):
    soma = sum(nascimentos[:dia])
    if nascimentos[dia] > soma and resposta == False:
        resposta = dia