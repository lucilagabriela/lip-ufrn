divisores = []
n = int(input('Infome o número: '))
for x in range(1, n+1):
    if n%x == 0:
        divisores.append(x)
print(divisores)