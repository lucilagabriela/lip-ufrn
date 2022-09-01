cidades = []
nmrCity = int(input('Quantas cidades você já visitou? '))
for x in range(nmrCity):
    city = input('Qual o nome da cidade? ')
    cidades.append(city)

cidades.reverse()
for x in range(nmrCity):
    print(cidades[x])