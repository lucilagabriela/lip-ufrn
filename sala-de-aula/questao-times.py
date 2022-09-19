# gravar 10 times e colocá-los em uma lista.
# armazenar em uma nova lista os libertadores.
# armazenar em uma outra lista os rebaixados.
# imprimir o maior nome
# imprimir confrontos 1º x 20º e 2º x 19º

times = []
libertadores = []
rebaixados = []
maiorNome = 0

for x in range(10):
    time = input('Digite o nome do time: ')
    times.append(time)
    len(times[x])
    if len(times[x]) > maiorNome:
        maiorNome = len(times[x])
libertadores = times[:3]
print(f'Os times do libertadores são: {libertadores}')
rebaixados = times[-4:]
print(f'Os times rebaixados foram: {rebaixados}')
print(maiorNome)
