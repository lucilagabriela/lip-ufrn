# Separando os 'perfeitos'
# Receba do usuário uma lista de valores inteiros com n elementos. A partir desta lista, gere duas listas auxiliares. Uma contendo seus elementos que são número perfeitos e outros contendo os que não são. Um número perfeito é aquele cuja soma de seus divisores, excluindo ele mesmo, é igual ao próprio número. Por exemplo: 6 = 1 + 2 + 3
n = int(input(''))
numeros = []
for x in range(n):
  valor = int(input(''))
  numeros.append(valor)
perfeitos = [] #perfeitos
naoPerfeitos = [] #nao perfeitos

for numero in numeros:
  soma = 0
  for divisor in range(1, numero):
    if numero%divisor == 0:
      soma += divisor
  if soma == numero:
      perfeitos.append(numero)
  else:
    naoPerfeitos.append(numero)
print(f'perfeitos = {perfeitos}')
print(f'não-perfeitos = {naoPerfeitos}')