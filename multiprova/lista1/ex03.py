# Pedro está fazendo uma viagem que passa por várias cidades. Neste programa, você deve ler um número inteiro N e então ler o nome das N cidades que Pedro já visitou (o nome de cada cidade será fornecido em uma linha separada). Em seguida, o seu programa deve imprimir a lista de cidades visitadas por Pedro em ordem alfabética.

cidades = []
N = int(input('')) # quantidade de cidades visitadas
for x in range(N):
    cidade = input('') # nome da cidade
    cidades.append(cidade)
cidades.sort() # ordem alfabética
for x in range(N):
    print(cidades[x]) # dentro dos [] deve haver o x do laço