numeros = []
nmrFinal = int(input('Qual é o número final? '))
for x in range(1, nmrFinal+1):
    numeros.append(x)
print(f'O menor número é {min(numeros)}')
print(f'O maior número é {max(numeros)}')
print(f'A soma de todos os números é {sum(numeros)}')